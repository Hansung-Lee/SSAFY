# Project 05

## 1. 목표
- 영화 추천 사이트의 세부 페이지 구성
- Template Variable을 활용한 Template 제작

## 2. 준비 사항
1. Python Web Framework 사용

## 3. 요구 사항

## 4. 결과 예시

#### - 프로젝트 파일 리스트
- Project_5
    - README.md : 프로젝트에 대한 설명문  
    - project_5/settings.py
    	- 언어, 시간을 한국어, 서울(GMT+09:00)로 설정
    	- ALLOWED_HOST는 모두 허용

    - detail/urls.py: urlpatterns에 각 페이지들의 path를 등록

    - detail/views.py: 각 페이지로 접속시 실행할 파이썬코드를 정의

    - detail/templates/base.html
        - html 기본 템플릿
    	- Bootstrap을 CDN 경로로 추가하고 Navbar를 생성

    - detail/templates/index.html
        - 내 홈페이지 메인 페이지
    	- 시맨틱 태그 header와 footer로 구성되어있음

    - detail/templates/qna.html
        - 사용자의 질문을 받기 위한 페이지
    	- 제목, 이메일, 내용을 입력하여 질문 등록가능
    	- 992px 보다 작은 화면에서 form의 형식이 바뀌도록 반응형 웹으로 디자인

    - detail/templates/mypage.html
        - 유저 정보를 출력하는 페이지
    	- 화면 좌측에는 사용자의 정보, 우측에는 사용자가 작성한 글의 목록을 보여줌

    - detail/templates/signup.html
        - 회원가입 페이지
    	- 이메일, 이름, 비밀번호, 비밀번호 확인을 입력하여 회원가입가능
    	- Bootstrap 그리드 시스템을 사용하여 좌측엔 이미지, 우측엔 form으로 정렬

    - detail/templates/error404.html
        - 위에서 만든 경로를 제외한 다른 요청이 들어오면 보여줄 404페이지
    	- 사용자가 잘못 입력한 경로를 잘못된 경로라고 표시해줌

    - detail/static/css/style.css: html의 style을 위한 css파일

    - detail/static/img: 홈페이지에 필요한 이미지 모음 디렉토리