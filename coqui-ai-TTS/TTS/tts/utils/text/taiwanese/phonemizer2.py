from typing import List
import jieba
import requests
import time

from .tailuoToPhonemes import PINYIN_DICT


from typing import List
import requests

from typing import List
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import re

def _chinese_character_to_pinyin(text: str) -> List[List[str]]:
    # APIのURL
    api_url = "http://tts001.iptcloud.net:8804/display"
    #api_url = "https://learn-language.tokyo/api/tailuo-tone-python"
    
    
    # リトライ設定
    retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retries)
    session = requests.Session()
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    # APIへのリクエスト
    response = session.get(api_url, params={"text0": text}, timeout=10)  # 10秒のタイムアウト
    #response = session.get(api_url, params={"text": text}, timeout=10)
    response.raise_for_status()  # ステータスコードが200でない場合、例外を発生させる
    print(f'api-text- {response.text}')
    # APIからの応答を受け取り、カンマで分割
    #pinyin_list = response.text.strip().split(',')
    #pinyin_list = re.split('[, -\.]',response.text)

    # ネストされたリスト形式に変換
    #pinyins = [item for item in pinyin_list if item]  # 空の要素は除外


    pinyin_list = re.split('([,，.。-])', response.text)
    pinyins = [item if item in {',', '，', '.', '。', '-'} else f'{item.strip()} ' for item in pinyin_list if item]
    pinyins_final = [pinyin.replace(',', '， ').replace('.', '。 ') for pinyin in pinyins]


    print(f'pinyins_flat_list- {pinyins_final}')
    return pinyins_final




def _chinese_pinyin_to_phoneme(pinyin: str) -> str:
    segment = pinyin[:-1]
    tone = pinyin[-1]
    phoneme = PINYIN_DICT.get(segment, [""])[0]
    print(f'pinyin- {segment}')
    print(f'shisei- {tone}')
    print(f'onso- {phoneme}')
    #return phoneme + tone
    return phoneme


def chinese_text_to_phonemes(text: str, seperator: str = "|") -> str:
    tokenized_text = jieba.cut(text, HMM=False)
    print(f'tokenized_text1- {tokenized_text}')
    tokenized_text = " ".join(tokenized_text)
    print(f'tokenized_text2- {tokenized_text}')
    pinyined_text: List[str] = _chinese_character_to_pinyin(tokenized_text)
    print(f'pinyined_text3- {pinyined_text}')

    results: List[str] = []

    for token in pinyined_text:
        print(f'token - {token}')
        if token[-1] in "12345678":  # TODO is_pinyin() に変換する
            pinyin_phonemes = _chinese_pinyin_to_phoneme(token)
            print(f'onso to shisei - {pinyin_phonemes}')

            results += list(pinyin_phonemes)
        else:  # is ponctuation or other
            results += list(token)
    print(f'results- {results}')
    return seperator.join(results)
