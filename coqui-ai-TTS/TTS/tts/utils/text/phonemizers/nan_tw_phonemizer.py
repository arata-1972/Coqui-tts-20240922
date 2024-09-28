from typing import Dict

#from TTS.tts.utils.text.taiwanese.phonemizer import chinese_text_to_phonemes, format_phonemized_text
#from TTS.tts.utils.text.taiwanese.phonemizer import chinese_text_to_phonemes
#from TTS.tts.utils.text.taiwanese.phonemizer import chinese_text_to_phonemes, save_skip_list_to_excel
from TTS.tts.utils.text.taiwanese.phonemizer import chinese_text_to_phonemes, save_skip_list_to_excel, skip_list


from TTS.tts.utils.text.phonemizers.base import BasePhonemizer

_DEF_ZH_PUNCS = "、.,[]()?!〽~『』「」【】"


class NAN_TW_Phonemizer(BasePhonemizer):
    """🐸TTS Zh-Cn 発音記号化器、`TTS.tts.utils.text.chinese_mandarin.phonemizer` の関数を使用

    引数:
        punctuations (str):
            句読点として扱う文字のセット。デフォルトは `_DEF_ZH_PUNCS`。

        keep_puncs (bool):
            True の場合、発音記号化後に句読点を保持します。デフォルトは False。

    例 ::

        "这是，样本中文。" -> `d|ʒ|ø|4| |ʂ|ʏ|4| |，| |i|ɑ|ŋ|4|b|œ|n|3| |d|ʒ|o|ŋ|1|w|œ|n|2| |。`

    TODO: 中国語の知識がある人がこの実装を確認する必要があります
    """

    language = "nan-tw"

    def __init__(self, punctuations=_DEF_ZH_PUNCS, keep_puncs=False, **kwargs):  # pylint: disable=unused-argument
        super().__init__(self.language, punctuations=punctuations, keep_puncs=keep_puncs)
        print("ここにきた1 NAN_TW_Phonemizer initialized")

    @staticmethod
    def name():
        print('ここにきた2 nan_tw_phonemizer')
        return "nan_tw_phonemizer"

   # @staticmethod
   # def phonemize_nan_tw(text: str, separator: str = "|") -> str:
   #     print('phonemize_nan_tw0',text)
   #     print('phonemize_nan_tw1',separator)
   #     ph = chinese_text_to_phonemes(text, separator)
   #     print(f'kextuka phonemize_nan_tw-',ph)
   #     return ph
    
    @staticmethod
    def phonemize_nan_tw(text: str, separator: str = "|") -> str:
        print('テキスト===     ',text)
        print('セパレーター===     ',separator)
        ph = chinese_text_to_phonemes(text, separator)
        #決め打ちで試す
        #ph = chinese_text_to_phonemes(text, "|")
        print(f'結果 = ',ph)
        return ph
    
    def _phonemize(self, text, separator):
        result = self.phonemize_nan_tw(text, separator)
        # すべての処理が終わった後に一度だけExcelに保存
        if skip_list:
            save_skip_list_to_excel()
        #return self.phonemize_nan_tw(text, separator)
        return result
    
    @staticmethod
    def supported_languages() -> Dict:
        return {"nan-tw": "Taiwanese (Taiwan)"}

    def version(self) -> str:
        return "0.0.1"

    def is_available(self) -> bool:
        return True


#if __name__ == "__main__":
#    text = "阿英，好來食晝矣。"
#    e = NAN_TW_Phonemizer()
#    print("test1===",e.supported_languages())
#    print("test2===",e.version())
#    print("test3===",e.language)
#    print("test4===",e.name())
#    print("test5===",e.is_available())
#    print("test6===","`" + e.phonemize(text) + "`")

