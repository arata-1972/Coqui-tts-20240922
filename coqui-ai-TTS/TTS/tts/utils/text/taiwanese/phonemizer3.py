from typing import List
import jieba
import requests
import time

from .tailuoToPhonemes import PINYIN_DICT

API_URL = "https://learn-language.tokyo/api/tailuo-tone-python"
RETRY_LIMIT = 5  # リトライ回数を増加
TIMEOUT = 10  # タイムアウト時間を延長

def _chinese_character_to_tailuo(text: str) -> List[str]:
    for attempt in range(RETRY_LIMIT):
        try:
            response = requests.get(API_URL, params={'text': text}, timeout=TIMEOUT)
            if response.status_code == 200:
                tailuo_list = response.json()  # JSONとしてレスポンスを受け取る
                print(f'tailuo_list- {tailuo_list}')
                return tailuo_list
            else:
                print(f'Error: Unable to get Tailuo from API, status code: {response.status_code}')
        except requests.Timeout:
            print(f'Request timed out. Attempt {attempt + 1} of {RETRY_LIMIT}')
        except requests.RequestException as e:
            print(f'Request failed: {e}')
        time.sleep(5)  # 待機時間を延長
    print(f'Error: Failed to get Tailuo after {RETRY_LIMIT} attempts')
    return []

def _tailuo_to_phoneme(tailuo: str) -> str:
    if len(tailuo) < 2:
        return tailuo
    segment = tailuo[:-1]
    tone = tailuo[-1]
    phoneme = PINYIN_DICT.get(segment, [""])[0]
    print(f'tailuo- {segment}')
    print(f'shisei- {tone}')
    print(f'onso- {phoneme}')
    return phoneme + tone

#def chinese_text_to_phonemes(text: str, separator: str = "|") -> str:
    #tokenized_text = jieba.cut(text, HMM=False)
    #print(f'tokenized_text1- {tokenized_text}')
    #tokenized_text = " ".join(tokenized_text)
    #print(f'tokenized_text2- {tokenized_text}')
    #tailuo_text: List[str] = _chinese_character_to_tailuo(tokenized_text)
    #print(f'tailuo_text3- {tailuo_text}')

    #results: List[str] = []

    #for token in tailuo_text:
        #print(f'token1- {token}')
     #   if token and token[-1] in "12345":
     #       tailuo_phonemes = _tailuo_to_phoneme(token)
     #      print(f'onso to shisei - {tailuo_phonemes}')
     #      results += list(tailuo_phonemes)
            
     #   else:
     #       results.append(token)  # スペースや他の記号もそのまま追加
    #print(f'results- {results}')
    #return separator.join(results)


def chinese_text_to_phonemes(text: str, separator: str = "|") -> str:
    tokenized_text = jieba.cut(text, HMM=False)
    print(f'tokenized_text1- {tokenized_text}')
    tokenized_text = " ".join(tokenized_text)
    print(f'tokenized_text2- {tokenized_text}')
    tailuo_text: List[str] = _chinese_character_to_tailuo(tokenized_text)
    print(f'tailuo_text3- {tailuo_text}')

    results: List[str] = []

    for token in tailuo_text:
        if token and token[-1] in "12345":
            tailuo_phonemes = _tailuo_to_phoneme(token)
            print(f'onso to shisei - {tailuo_phonemes}')
            results += list(tailuo_phonemes)
        else:
            results.append(token)  # スペースや他の記号もそのまま追加
    print(f'results- {results}')
    
    # 空の文字列を無視せず、必要な場所にスペースを挿入する
    final_phonemized_text = ''.join([r if r else ' ' for r in results])
    return final_phonemized_text







