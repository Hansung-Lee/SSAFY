# Project 03

## 1. 목표
- 영진위 API를 활용하여 수집한 데이터를 데이터베이스에 반영하기
- SQL을 통한 데이터베이스 조작
- 단일 테이블에서의 데이터 조작
- 영화추천서비스와 관련된 다양한 검색 쿼리 작성하기

## 2. 준비 사항
1. SQL 활용 환경 설정
2. 영화 데이터 베이스

## 3. 요구 사항

## 4. 결과 예시

#### - 프로젝트 파일 리스트
- Project_3
    - README.md : 프로젝트에 대한 설명문  

    - 01_create_table.sql
    	- 영화의 정보를 저장하기 위한 테이블 구성(CREATE TABLE) sql문 작성
    	- 주어진 csv 파일을 import 하여 데이터베이스 구축

    - 02_crud.sql
        - 누락된 영화 정보를 추가로 입력하는 sql문 작성
        - 과거의 데이터 삭제 및 NULL 인 값음 '없음'으로 수정

    - 03_select.sql
        - 6가지 조건에 따라 데이터베이스의 내용 출력(SELECT) sql문 작성
        	- 상영시간 >= 150
        	- 장르 = 애니메이션
        	- 제작국가 = 덴마크, 장르 = 애니메이션
        	- 누적관객수 > 1,000,000, 관람등급 = 청소년관람불가
        	- 20000101< 개봉연도 < 20091231
        	- 장르를 중복없이 출력

	- 04_expression.sql
		- 5가지 연산에 따라 데이터베이스의 내용 출력(SELECT) sql문 작성
        	- 총 누적관객수
        	- 가장 많은 누적관객수
        	- 가장 상영시간이 짧은 영화
        	- 평균 누적관객수
        	- 영화의 개수
	
	- 05_order.sql
		- 3가지 정렬에 따라 데이터베이스의 내용 출력(SELECT) sql문 작성
        	- 누적관객수(내림차순)
        	- 제작국가(오름차순), 누적관객수(내림차순)
        	- 상영시간(내림차순)

	- pjt.sqlite3 : 영진위 API를 활용하여 수집한 데이터베이스