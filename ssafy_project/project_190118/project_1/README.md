# Project 01

## 1. 목표
- 기초 Python에 대한 이해
- Python을 통한 데이터 수집 및 파일 저장
- 웹 크롤러 및 API 활용을 통해 데이터를 수집하고 내가 원하는 형태로 가공한다.
- 영화평점사이트(예- watcha)에 필요한 데이터를 프로그래밍을 통해 수집한다.

## 2. 준비 사항
1. Python 환경 설정
    - python 3.6 이상
2. 필수 라이브러리 활용
    - requests
3. 필수 API
    - 영화진흥위원회 오픈 API
        - 주간/주말 박스오피스 API 서비스
        - 영화 상세정보 API 서비스
    - 네이버 영화 검색 API

## 3. 요구 사항

## 4. 결과 예시

#### - 활용한 API
- 영화진흥위원회 오픈 API (주간/주말 박스오피스, 영화 상세정보)
	- URL : http://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do
	- 주간/주말 박스오피스 API를 활용하여 최근 10주간 박스오피스 TOP10 데이터를 수집함
	- 영화 상세정보 API를 활용하여 위에서 수집한 영화의 상세정보 데이터를 수집함
- 네이버 영화 검색 API
	- URL : https://developers.naver.com/docs/search/movie/
	- 검색(영화) API를 활용하여 위에서 수집한 영화의 추가 데이터를 수집함
	- 여기서 추가 데이터란, 포스터 이미지 URL과 유저 평점을 포함함


#### - 프로젝트 파일 리스트
- Project_1
    - README.md : 프로젝트에 대한 설명문

    - movieapi.py : 파이썬 메인 파일, API를 활용하여 데이터를 수집함

    - boxoffice.csv
        - 영화진흥위원회 오픈 API(주간/주말 박스오피스)를 이용하여 박스오피스 데이터를 받아옴
        - 'movie_code','title','audience','recorded_at' 의 컬럼명으로 저장
        - 각 컬럼은 영화 대표코드 , 영화명 , 해당일 누적관객수 , 해당일을 뜻함

    - movie.csv
        - 영화진흥위원회 오픈 API(영화상세정보)를 이용하여 영화정보 데이터를 받아옴
        - 'movie_code','movie_name_ko','movie_name_en','movie_name_og','prdt_year','genres','directors','watch_grade_nm','actor1','actor2','actor3' 의 컬럼명으로 저장
        - 각 컬럼은 영화 대표코드 , 영화명(국문) , 영화명(영문) , 영화명(원문) , 개봉연도 , 상영시간 , 장르 , 감독명 , 관람등급 , 배우1 , 배우2 , 배우3을 뜻함

    - movie_naver.csv
        - 네이버 영화 검색 API를 이용하여 영화정보 데이터를 받아옴
        - 'movie_code','thumb_url','link_url','user_rating' 의 컬럼명으로 저장
        - 각 컬럼은 영진위 영화 대표코드 , 영화 썸네일 이미지의 URL , 하이퍼텍스트 link , 유저 평점을 뜻함

    - images/ : 앞서 네이버 영화 검색 API를 통해 얻은 영화 썸네일 이미지의 URL에 요청을 보내 실제 이미지 파일로 저장함