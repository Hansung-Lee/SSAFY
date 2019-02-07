# Project 04_mini

## 1. 목표
- 데이터를 생성, 조회, 삭제, 수정할 수 있는 Web Application 제작
- sqlite3를 통한 데이터 조작

## 2. 준비 사항
1. Flask Framework 사용을 위한 환경 설정
2. 영화 데이터 베이스

## 3. 요구 사항

## 4. 결과 예시

#### - 프로젝트 파일 리스트
- Project_4
    - README.md : 프로젝트에 대한 설명문  
    - app.py
    	- flask를 이용하여 블로그를 만들기위한 python 코드
    	- sqlite3을 이용하여 블로그 게시글 데이터 관리
    
	- blog.db : 블로그 게시글을 저장하는 데이터베이스  
	
    - templates/articles.html
    	- 글 목록 페이지
    	- 현재 데이터베이스에 저장되어 있는 게시글을 모두 보여줌

    - templates/detail.html
        - 글 상세 페이지
    	- 선택한 게시글의 상세 내역을 보여줌

    - templates/edit.html
        - 글 수정 페이지
    	- 선택한 게시글의 정보를 수정할 수 있음

    - templates/new.html
        - 새 글 생성 페이지
        - 새로운 글을 작성하여 데이터베이스에 추가

    - templates/success.html
        - 글 생성 완료 페이지
        - 글 생성 완료 메시지와 함께 목록으로 이동할 수 있는 버튼 제공