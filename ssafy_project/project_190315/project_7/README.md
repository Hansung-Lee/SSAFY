# Project 07

## 1. 목표
- 데이터를 생성, 조회, 삭제, 수정할 수 있는 Web Application 제작
- 데이터베이스 테이블간 관계 설정 (1:N)

## 2. 준비 사항
1. Python Web Framework
2. 샘플 영화 정보

## 3. 요구 사항

## 4. 결과 예시

#### - 프로젝트 파일 리스트
- Project_7
    - README.md : 프로젝트에 대한 설명문  
    
	- db.sqlite3: 영화 정보 데이터를 저장하는 데이터베이스
		
	- movies/models.py: 데이터베이스에 Movie 테이블을 만듬
		
	- movies/urls.py: urlpatterns에 각 페이지들의 path를 등록
	
	- movies/views.py: 각 페이지로 접속시 실행할 파이썬코드를 정의
		
    - movies/templates/base.html : 기본 html 템플릿, Bootstrap css 로드와 Navbar를 포함

    - movies/templates/index.html
    	- 영화 목록 페이지
    	- 현재 데이터베이스에 저장되어 있는 영화의 포스터이미지, 제목, 평점을 보여줌

    - movies/templates/detail.html
        - 영화 정보 조회 페이지
    	- 선택한 영화의 모든 정보를 보여줌

    - movies/templates/edit.html
        - 영화 정보 수정 페이지
    	- 선택한 영화의 정보를 수정할 수 있음