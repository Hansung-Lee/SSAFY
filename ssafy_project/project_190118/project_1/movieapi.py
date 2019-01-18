import datetime
import requests
import os

# API key 불러오기
movie_key = os.getenv('movie_key')
naver_id = os.getenv('naver_id')
naver_secret = os.getenv('naver_secret')


# 1. 영화진흥위원회 오픈 API(주간/주말 박스오피스 데이터)

today = list(map(int,str(datetime.date.today()).split('-'))) # 오늘 날짜
whatday = datetime.date(today[0],today[1],today[2]).weekday() # 오늘의 요일


# 최근 일요일을 찾고 최근 10주치 일요일 날짜를 리스트에 저장
day = []
day_cnt = 0
if whatday == 6:
    for i in range(10):
        day.append(''.join(str(datetime.date.today()-datetime.timedelta(days=day_cnt)).split('-')))
        day_cnt+=7
else:
    for i in range(10):
        day.append(''.join(str(datetime.date.today()-datetime.timedelta(days=(1+whatday)+day_cnt)).split('-')))
        day_cnt+=7


# 영화진흥위원회 오픈 API(주간/주말 박스오피스 데이터)를 이용하여 박스오피스 데이터를 받아옴
# 'movie_code','title','audience','recorded_at' 의 컬럼명으로 저장
# 각 컬럼은 영화 대표코드 , 영화명 , 해당일 누적관객수 , 해당일을 뜻함
li_boxoffice = []
for d in day:
    url_movie = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={}&targetDt={}&weekGb=0".format(movie_key, d)

    res = requests.get(url_movie)
    res_data = res.json().get('boxOfficeResult').get('weeklyBoxOfficeList')
    
    for movie in res_data:
        li_boxoffice.append({
            'movie_code' : movie.get('movieCd'),
            'title' : movie.get('movieNm'),
            'audience' : movie.get('audiAcc'),
            'recorded_at' : d
        })


# 중복되는 영화 데이터는 해당일, 누적관객수를 최근 데이터로 갱신
# 중복되는 영화 삭제
new_boxoffice = []
movie_code = [] # 중복되는 영화인지 검색하기 위한 비교 리스트 겸 2.를 위한 대표코드 저장
for bo in li_boxoffice:
    if bo.get('movie_code') in movie_code:
        pass
    else:
        new_boxoffice.append(bo)
        movie_code.append(bo.get('movie_code'))


# csv 파일로 저장
import csv

with open('boxoffice.csv', 'w') as f:
    field = ('movie_code','title','audience','recorded_at')
    writer = csv.DictWriter(f, fieldnames=field)
    writer.writeheader()
    for l in new_boxoffice:
        writer.writerow(l)
        
        
        
        
# 2. 영화진흥위원회 오픈 API(영화 상세정보)

# 영화진흥위원회 오픈 API를 이용하여 영화정보 데이터를 받아옴
# 'movie_code','movie_name_ko','movie_name_en','movie_name_og','prdt_year','genres','directors','watch_grade_nm','actor1','actor2','actor3' 의 컬럼명으로 저장
# 각 컬럼은 영화 대표코드 , 영화명(국문) , 영화명(영문) , 영화명(원문) , 개봉연도 , 상영시간 , 장르 , 감독명 , 관람등급 , 배우1 , 배우2 , 배우3을 뜻함
li_movie_detail = []
for mc in movie_code:
    url_movie = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={}&movieCd={}".format(movie_key, mc)
    
    res = requests.get(url_movie)
    res_data = res.json().get('movieInfoResult').get('movieInfo')
    
    # 배우가 3명이 아닐수도 있으니 배우명 먼저 저장
    # 만약 3명 미만이면 남은 actor 변수에 ' ' 띄어쓰기를 넣어줌
    li_actor = []
    for i in range(len(res_data.get('actors'))):
        li_actor.append(res_data.get('actors')[i].get('peopleNm'))
        
    for i in range(3-len(res_data.get('actors'))):
        li_actor.append(' ')
    
    li_movie_detail.append({
        'movie_code' : res_data.get('movieCd'),
        'movie_name_ko' : res_data.get('movieNm'),
        'movie_name_en' : res_data.get('movieNmEn'),
        'movie_name_og' : res_data.get('movieNmOg'),
        'prdt_year' : res_data.get('prdtYear'),
        'genres' : res_data.get('genres')[0].get('genreNm'),
        'directors' : res_data.get('directors')[0].get('peopleNm'),
        'watch_grade_nm' : res_data.get('audits')[0].get('watchGradeNm'),
        'actor1' : li_actor[0],
        'actor2' : li_actor[1],
        'actor3' : li_actor[2]
    })
    
# csv 파일로 저장
with open('movie.csv', 'w') as f:
    field = ('movie_code','movie_name_ko','movie_name_en','movie_name_og','prdt_year','genres','directors','watch_grade_nm','actor1','actor2','actor3')
    writer = csv.DictWriter(f, fieldnames=field)
    writer.writeheader()
    for l in li_movie_detail:
        writer.writerow(l)
        


# 3. 네이버 영화 검색 API
headers_naver = {
    'X-Naver-Client-Id': naver_id,
    'X-Naver-Client-Secret': naver_secret
}

# 네이버 영화 검색 API를 이용하여 영화정보 데이터를 받아옴
# 'movie_code','thumb_url','link_url','user_rating' 의 컬럼명으로 저장
# 각 컬럼은 영진위 영화 대표코드 , 영화 썸네일 이미지의 URL , 하이퍼텍스트 link , 유저 평점을 뜻함
li_naver = []

for i in range(len(li_movie_detail)):
    url_naver = "https://openapi.naver.com/v1/search/movie.json?query={}".format(li_movie_detail[i].get('movie_name_ko'))
    
    res = requests.get(url_naver, headers=headers_naver)
    res_data = res.json().get('items')
    
    if res_data:
        res_data = res_data[0]
        li_naver.append({
        'movie_code' : movie_code[i],
        'thumb_url' : res_data.get('image'),
        'link_url' : res_data.get('link'),
        'user_rating' : res_data.get('userRating')
        })
    

# csv 파일로 저장
with open('movie_naver.csv', 'w') as f:
    field = ('movie_code','thumb_url','link_url','user_rating')
    writer = csv.DictWriter(f, fieldnames=field)
    writer.writeheader()
    for l in li_naver:
        writer.writerow(l)



# 4. 영화 포스터 이미지 저장
for n in li_naver:
    if (len(n)==0):
        continue
    else:
        with open('images/{}.jpg'.format(n.get('movie_code')), 'wb') as handle:
            response = requests.get(n.get('thumb_url'), stream=True)
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)