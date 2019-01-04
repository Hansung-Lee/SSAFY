# 인식시킬 사진을 clova API를 통해 요청을 보내, 인식 결과를 받아온다.
# req (파일)

# 1. requests를 통해 clova API 주소에 요청을 보낸다.
# 2. 응답 받은 json을 파싱하여 원하는 결과를 출력한다.


import requests
import os


url = "https://openapi.naver.com/v1/vision/celebrity"

naver_id = os.getenv("NAVER_ID")
naver_secret = os.getenv("NAVER_SECRET")


img_url = 'https://upload.wikimedia.org/wikipedia/commons/e/e9/Official_portrait_of_Barack_Obama.jpg'

# 1. 해당하는 img_url에 요청을 보내서, 
# 2. 파일데이터를 받아 저장해 둔다.
img = requests.get(img_url, stream=True).content

# img = requests.get(img_url, stream=True).raw.read()
# img = requests.get(img_url).content # 이미지 url로 인식시키는 방법
# img = open('iu1.jpg', 'rb') # 이미지 파일로 인식시키는 방법

headers = {
        'X-Naver-Client-Id': naver_id,
        'X-Naver-Client-Secret': naver_secret
    }
    
files = {
    'image': img
}
    
res = requests.post(url, headers=headers, files=files)

# json => dictionary

# => XXX입니다. XX% 확신할 수 있습니다.
# str -> float -> round

# String 조작
# 합체: concatenation
# "happy" + "hacking"
# "PP" + "AP"

# 수술: interpolation(보간법)
# name = "john"
# greeting = "Hello {}".format(name)




celebrity = res.json().get('faces')[0].get('celebrity').get('value')
confidence = round(res.json().get('faces')[0].get('celebrity').get('confidence') * 100)

# print('인식된 인물은 "' + celebrity + '" 입니다. ' + str(confidence) + '% 확신할 수 있습니다.')
print('인식된 인물은 "{}" 입니다. {}% 확신할 수 있습니다.'.format(celebrity, confidence))