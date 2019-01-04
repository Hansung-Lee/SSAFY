
# 네이버(파파고)야 내가 단어하나 전달할테니, 번역해줘

# 0. 사용자에게 단어를 입력받는다. (추가기능)
# 1. papago API 요청 주소에 요청을 보낸다.
# 2. 응답을 받아 번역된 단어를 출력한다.


import requests
import os
from pprint import pprint as pp

# 함수를 import하는 방법
# import pprint => pprint.pprint()
# from pprint import pprint => pprint()
# from pprint import pprint as pp => pp()



url = "https://openapi.naver.com/v1/papago/n2mt"

naver_id = os.getenv("NAVER_ID")
naver_secret = os.getenv("NAVER_SECRET")
# naver_secret = os.environ.get('NAVER_SECRET')

sel = ''

sel = input("1. 한글->영어 번역  2. 영어->한글 번역\n")



if (sel=='1'):
    input_text = input("번역할 한글 단어를 입력하세요.\n")
    
    headers = {
        'X-Naver-Client-Id': naver_id,
        'X-Naver-Client-Secret': naver_secret
    }
    
    data = {
        'source': 'ko',
        'target': 'en',
        'text': input_text
    }


elif (sel=='2'):
    input_text = input("번역할 영어 단어를 입력하세요.\n")
    
    headers = {
        'X-Naver-Client-Id': naver_id,
        'X-Naver-Client-Secret': naver_secret
    }
    
    data = {
        'source': 'en',
        'target': 'ko',
        'text': input_text
    }

else :
    print('잘못된 입력입니다. 다시 시도해주세요.')

try :
    res = requests.post(url, headers=headers, data=data)

    pp(res.json().get('message').get('result').get('translatedText'))  # 값이 빈경우 None 출력
    # pp(res.json()['message']['result']['translatedText']) # 값이 빈경우 NoneType에러
    # print(res.text.split('"')[27])

except NameError:
    print('', end = '')
except AttributeError:
    print('API 연결 오류')


