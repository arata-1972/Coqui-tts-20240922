import os
from trainer import Trainer, TrainerArgs

from TTS.tts.configs.glow_tts_config import GlowTTSConfig
from TTS.tts.configs.shared_configs import BaseDatasetConfig
from TTS.tts.datasets import load_tts_samples
from TTS.tts.models.glow_tts import GlowTTS
from TTS.tts.utils.text.tokenizer import TTSTokenizer
from TTS.utils.audio import AudioProcessor
from multiprocessing import Process, freeze_support

from TTS.tts.configs.tacotron2_config import Tacotron2Config
from TTS.tts.models.tacotron2 import Tacotron2

from TTS.tts.configs.vits_config import VitsConfig
from TTS.tts.models.vits import Vits

import torch
import torch.nn.utils as utils

import os
os.environ['CUDA_LAUNCH_BLOCKING'] = '1'


# CUDAメモリ管理の設定
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"
torch.cuda.empty_cache()

# スクリプトのディレクトリをトレーニングフォルダとして使用
output_path = os.path.dirname(os.path.abspath(__file__))

# データセットの設定
dataset_config = BaseDatasetConfig(
    formatter="ljspeech",  # LJSpeech形式でフォーマット
    meta_file_train="metadata.csv",  # メタデータファイルのパス
    path=os.path.join(output_path, "../recipes/ljspeech/LJSpeech-1.1/")
)

# トレーニング設定の初期化
config = VitsConfig(
#config = Tacotron2Config(
#config = GlowTTSConfig(
    batch_size=8,
    eval_batch_size=4,
    num_loader_workers=4,
    num_eval_loader_workers=4,
    run_eval=True,
    test_delay_epochs=-1,
    epochs=1000,
    text_cleaner="chinese_mandarin_cleaners",
    #use_phonemes=False,
    use_phonemes=True,
    phoneme_language="nan-tw",

    eval_split_size=100,
    phoneme_cache_path=os.path.join(output_path, "phoneme_cache"),
    print_step=25,
    print_eval=False,
    mixed_precision=True,
    output_path=output_path,
    datasets=[dataset_config],
)
print(f"Config phonemizer: {config.phoneme_language}")
print(f"Config phonemizer: {config.phonemizer}")



# オーディオプロセッサの初期化
ap = AudioProcessor.init_from_config(config)

# トークナイザーの初期化
tokenizer, config = TTSTokenizer.init_from_config(config)


# オーディオの読み込み時にモノラルに変換
def load_audio_mono(audio_path, ap):
    wav = ap.load_wav(audio_path)
    if wav.ndim > 1:  # ステレオの場合、モノラルに変換
        wav = wav.mean(axis=1)
    return wav


# データローダーでテンソルの次元を合わせる部分の修正
def collate_fn(batch):
    max_len = max([wav.shape[-1] for wav in batch])  # 音声の最大長を取得
    wav_padded = torch.zeros((len(batch), 1, max_len))  # 1チャネルに強制
    for i, wav in enumerate(batch):
        if wav.ndim == 1:  # 1チャネル（モノラル）の場合
            wav = wav.unsqueeze(0)  # 次元を追加して3次元に
        wav_padded[i, :, :wav.shape[1]] = torch.FloatTensor(wav)
    return wav_padded


# オーディオファイルが存在するかを確認し、欠損ファイルを除外する関数
def filter_and_load_audio_files(samples, ap):
    valid_samples = []
    for sample in samples:
        audio_path = sample['audio_file']
        if os.path.exists(audio_path):
            wav = load_audio_mono(audio_path, ap)  # モノラルに変換
            sample['audio'] = wav  # オーディオデータをサンプルに追加
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

# データサンプルのロードと欠損ファイルの除外
train_samples = filter_and_load_audio_files(train_samples, ap)
eval_samples = filter_and_load_audio_files(eval_samples, ap)



# metadata.csvの内容を表示
with open(os.path.join(dataset_config.path, dataset_config.meta_file_train), 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i < 10:  # 最初の10行を表示
            print(line)

            

# トレーニングサンプルの最初の数件を表示
print(f"Train Samples: {train_samples[:5]}")
print(f"Eval Samples: {eval_samples[:5]}")

# サンプルが適切かどうかフィルタリング
#train_samples = [s for s in train_samples if len(s['text']) > 1]
#eval_samples = [s for s in eval_samples if len(s['text']) > 1]

print(f"トレーニングサンプル数: {len(train_samples)}")
print(f"評価サンプル数: {len(eval_samples)}")

# モデルの初期化
#model = GlowTTS(config, ap, tokenizer, speaker_manager=None)
model = Vits(config, ap, tokenizer, speaker_manager=None)
#model = Tacotron2(config, ap, tokenizer, speaker_manager=None)

# トレーナーの初期化
trainer = Trainer(
    TrainerArgs(), config, output_path, model=model, train_samples=train_samples, eval_samples=eval_samples
)

# トレーニング開始
trainer.fit()
