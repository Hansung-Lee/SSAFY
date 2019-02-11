# Project 04

## 1. 목표
- 데이터를 생성, 조회, 삭제, 수정할 수 있는 Web Application 제작
- Python Web Framework를 통한 데이터 조작
- Object Relational Mapping에 대한 이해
- Template Variable을 활용한 Template 제작
- 영화 추천 사이트의 영화 정보 데이터 관리

## 2. 준비 사항
1. Python Web Framework 선택 (Flask)
2. Python Web Framework 사용을 위한 환경 설정

## 3. 요구 사항

## 4. 결과 예시

#### - 프로젝트 파일 리스트
- Project_4
    - README.md : 프로젝트에 대한 설명문  
    - app.py
    	- flask를 이용하여 영화 추천 사이트를 만들기위한 python 코드
    	- flask_sqlalchemy를 이용하여 ORM 방식으로 영화 정보 데이터 관리
    
	- db_flask.sqlite3
		- 영화 정보 데이터를 저장하는 데이터베이스
		- 평점을 별로 나타내기 위해 평점별 별 이미지 테이블도 추가함
	
    - templates/base.html : 기본 html 템플릿, Bootstrap css 로드와 Navbar를 포함

    - templates/index.html
    	- 영화 목록 페이지
    	- 현재 데이터베이스에 저장되어 있는 영화의 포스터이미지, 제목, 평점을 보여줌

    - templates/detail.html
        - 영화 정보 조회 페이지
    	- 선택한 영화의 모든 정보를 보여줌

    - templates/edit.html
        - 영화 정보 수정 페이지
    	- 선택한 영화의 정보를 수정할 수 있음

    - templates/new.html
        - 영화 정보 생성 페이지
        - 새로운 영화 정보를 작성하여 데이터베이스에 추가

    - templates/success.html
        - 영화 정보 생성 완료 페이지
        - 영화 정보 생성 완료 메시지와 함께 목록으로 이동할 수 있는 버튼 제공