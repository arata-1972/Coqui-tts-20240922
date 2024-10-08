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

import re
import requests
from requests.adapters import HTTPAdapter
#from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from typing import List

import jieba
import requests
import re
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from typing import List
from .tailuoToPhonemes import PINYIN_DICT

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import re

import pandas as pd  # Excel保存のために追加

# スキップリストの定義
skip_list = []  # スキップリストをリスト形式で定義

def _chinese_character_to_pinyin(text: str) -> list:
    # APIのURL
    api_url = "https://learn-language.tokyo/api/tailuo-tone"
    
    # リトライ設定
    retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retries)
    session = requests.Session()
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    # APIへのリクエスト
    response = session.get(api_url, params={"text": text}, timeout=10)
    response.raise_for_status()  # ステータスコードが200でない場合、例外を発生させる
    api_text = response.text
    api_text = api_text.strip('"').strip("'")
    print(f'API response text: {api_text}')
    
    # 正規表現で区切り文字を含めて分割
    parts = re.split('([,，.。])', api_text)
    pinyins = []

    for part in parts:
        if part in {',', '，'}:
            pinyins.append(' ， ')
        elif part in {'.', '。'}:
            pinyins.append(' 。 ')
        else:
            # スペースによる分割とハイフンの処理
            elements = part.split()
            for element in elements:
                sub_parts = element.split('-')
                for i, sub_part in enumerate(sub_parts):
                    pinyins.append(sub_part.strip())
                    if i < len(sub_parts) - 1:
                        pinyins.append(' ')
                if elements.index(element) < len(elements) - 1:
                    pinyins.append(' ')

    print(f'pinyins_flat_list-  {pinyins}')
    return pinyins

def _chinese_pinyin_to_phoneme(pinyin: str, text: str) -> str:
    segment = pinyin[:-1]
    tone = pinyin[-1]
    phoneme = PINYIN_DICT.get(segment, [""])[0]
    
    # PINYIN_DICTに該当するデータがない場合、スキップする処理
    if phoneme == "":
        skip_list.append({'pinyin': segment, 'text': text})  # スキップしたpinyinとtextをリストに追加
        print(f'これで学習はされていないと想定')
        return ""  
    
    print(f'pinyin- {segment}')
    print(f'shisei- {tone}')
    print(f'onso- {phoneme}')
    print(f'これで学習はされていると想定')
    return phoneme + tone

def chinese_text_to_phonemes(text: str, seperator: str = "|") -> str:
    # jiebaの分かち書きをスキップ
    tokenized_text = text
    pinyined_text: List[str] = _chinese_character_to_pinyin(tokenized_text)

    results: List[str] = []

    for token in pinyined_text:
        print(f'token - {token}')
        if token and token[-1] in "12345678":  # ここでtokenが空でないか確認
            pinyin_phonemes = _chinese_pinyin_to_phoneme(token, text)  # textを渡す
            print(f'onso to shisei - {pinyin_phonemes}')

            results += list(pinyin_phonemes)
        else:  # is punctuation or other
            results += list(token)
    print(f'results- {seperator.join(results)}')
    return seperator.join(results)

# スキップリストをExcelに保存する関数
def save_skip_list_to_excel():
    if skip_list:
        # DataFrameに変換
        df = pd.DataFrame(skip_list)
        # 重複を除去してソート
        df = df.drop_duplicates().sort_values(by=['pinyin', 'text'])
        df.to_excel('skipped_words.xlsx', index=False)
        print("スキップされた単語と対応するテキストはskipped_words.xlsxに保存されました。")
    else:
        print("単語はスキップされませんでした。")
