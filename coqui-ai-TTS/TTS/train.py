import os
from trainer import Trainer, TrainerArgs
from TTS.tts.configs.shared_configs import BaseDatasetConfig
from TTS.tts.configs.vits_config import VitsConfig
from TTS.tts.datasets import load_tts_samples
from TTS.tts.models.vits import Vits, VitsAudioConfig
from TTS.tts.utils.text.tokenizer import TTSTokenizer
from TTS.utils.audio import AudioProcessor
from torch.optim.lr_scheduler import ReduceLROnPlateau

# 出力パスの設定
output_path = os.path.dirname(os.path.abspath(__file__))

# データセットの設定
dataset_config = BaseDatasetConfig(
    formatter="ljspeech", 
    meta_file_train="metadata.csv", 
    path=os.path.join(output_path, "../recipes/ljspeech/LJSpeech-1.1/")
)

# オーディオ設定
audio_config = VitsAudioConfig(
    sample_rate=22050, 
    win_length=1024, 
    hop_length=256, 
    num_mels=80,
    mel_fmin=50,  # 下限周波数
    mel_fmax=8000  # 上限周波数
)

# Vitsモデルの設定
config = VitsConfig(
    audio=audio_config,
    run_name="vits_ljspeech",
    batch_size=4,  # バッチサイズ
    eval_batch_size=2,
    batch_group_size=5,
    num_loader_workers=8,
    num_eval_loader_workers=4,
    run_eval=True,
    test_delay_epochs=-1,
    epochs=1000,
    text_cleaner="phoneme_cleaners",
    use_phonemes=True,
    phoneme_language="nan-tw",
    phoneme_cache_path=os.path.join(output_path, "phoneme_cache"),
    compute_input_seq_cache=True,
    print_step=25,
    print_eval=True,
    mixed_precision=False,  # 混合精度は無効化
    output_path=output_path,
    datasets=[dataset_config],
    cudnn_benchmark=False,
    eval_split_size=0.15,
    grad_clip=[0.05, 0.05],  # 勾配クリッピングをさらに強化
    lr_gen=0.000005,  # ジェネレータの学習率を低下
    lr_disc=0.000005,  # ディスクリミネータの学習率を低下
    optimizer="AdamW"  # AdamWを使用
)

# オーディオプロセッサの初期化
ap = AudioProcessor.init_from_config(config)

# トークナイザーの初期化
tokenizer, config = TTSTokenizer.init_from_config(config)

# オーディオの読み込み時にモノラルに変換する関数
def load_audio_mono(audio_path, ap):
    wav = ap.load_wav(audio_path)
    if wav.ndim > 1:  # ステレオの場合、モノラルに変換
        wav = wav.mean(axis=1)
    return wav

# データローダーでテンソルの次元を合わせる関数
def collate_fn(batch):
    max_len = max([wav.shape[-1] for wav in batch])  # 音声の最大長を取得
    wav_padded = torch.zeros((len(batch), 1, max_len))  # 1チャネルに強制
    for i, wav in enumerate(batch):
        if wav.ndim == 1:  # 1チャネル（モノラル）の場合
            wav = wav.unsqueeze(0)  # 次元を追加して3次元に
        wav_padded[i, :, :wav.shape[1]] = torch.FloatTensor(wav)
    return wav_padded

# メルスペクトログラムの異常値をフィルタリングする関数
def filter_and_load_audio_files(samples, ap):
    valid_samples = []
    THRESHOLD = 100  # メルスペクトログラムの最大値のしきい値を設定
    for sample in samples:
        audio_path = sample['audio_file']
        if os.path.exists(audio_path):
            wav = load_audio_mono(audio_path, ap)  # モノラルに変換
            sample['audio'] = wav  # オーディオデータをサンプルに追加
            if sample['mel'].max() < THRESHOLD:  # 異常値のフィルタリング
                valid_samples.append(sample)
        else:
            print(f"File not found, skipping: {audio_path}")
    return valid_samples

# データサンプルのロード
train_samples, eval_samples = load_tts_samples(
    dataset_config,
    eval_split=True,
    eval_split_max_size=config.eval_split_max_size,
    eval_split_size=config.eval_split_size,
)

# AudioProcessorを使って音声ファイルを読み込む
ap = AudioProcessor.init_from_config(config)

# データサンプルのロードと欠損ファイルの除外、異常値のフィルタリング
train_samples = filter_and_load_audio_files(train_samples, ap)
eval_samples = filter_and_load_audio_files(eval_samples, ap)

# metadata.csvの内容を表示
with open(os.path.join(dataset_config.path, dataset_config.meta_file_train), 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i < 10:  # 最初の10行を表示
            print(line)

# トレーニングサンプルと評価サンプルの数を表示
print(f"Train Samples: {train_samples[:5]}")
print(f"Eval Samples: {eval_samples[:5]}")
print(f"トレーニングサンプル数: {len(train_samples)}")
print(f"評価サンプル数: {len(eval_samples)}")

# Vitsモデルの初期化
model = Vits(config, ap, tokenizer, speaker_manager=None)

# 学習率スケジューラの設定
scheduler = ReduceLROnPlateau(
    optimizer=model.optimizer,  # モデルのオプティマイザを指定
    mode='min',  # 損失が減少する方向で調整
    factor=0.5,  # 学習率を半分に減少
    patience=10,  # 10エポック間改善がない場合
    verbose=True  # 学習率変更をログに表示
)

# トレーナーの初期化と学習の開始
trainer = Trainer(
    TrainerArgs(),
    config,
    output_path,
    model=model,
    train_samples=train_samples,
    eval_samples=eval_samples,
)

# トレーニングループ
for epoch in range(config.epochs):
    trainer.train_epoch()  # 1エポック分の学習を実行
    eval_loss = trainer.eval_epoch()  # 評価を実行
    scheduler.step(eval_loss)  # 損失に基づいて学習率を調整