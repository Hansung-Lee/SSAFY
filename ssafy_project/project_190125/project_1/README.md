# Project 02

## 1. 목표
- WEB 프론트엔드에 대한 이해
- 영화 추천 사이트를 위한 HTML를 통한 웹 페이지 마크업 및 레이아웃 구성
- CSS를 통한 선택자 활용 및 웹 페이지 꾸미기
- Bootstrap을 활용한 HTML/CSS, JS Component 활용
- 반응형 웹 페이지 구현

## 2. 준비 사항
1. HTML/CSS, Bootstrap 환경 구성
    - Text Editor(자유)
    - Bootstrap v.4.2.1
2. 웹 페이지를 위한 Assets 다운로드
    - assets 폴더에는 활용할 이미지가 있습니다.
    - data 는 구글 스프레드 시트로 입력해야 할 내용이 작성되어 있습니다.
    - 예시이미지 는 결과물 이미지가 있습니다.

## 3. 요구 사항

## 4. 결과 예시

#### - 프로젝트 파일 리스트
- Project_2
    - README.md : 프로젝트에 대한 설명문  

    - 01_layout.html
    	- Bootstrap을 사용하기 위해 <head> 안에 선언
    	- 최상단에 Sticky navigation bar가 위치하여 스크롤을 아래로 내리더라도 navigation bar 이용 가능
    	- Navbar 아래에 배경이미지와 텍스트를 포함한 header가 위치
    	- 최하단에 내 이름과 헤더로 올라가는 이미지 버튼을 포함한 Footer가 위치

    - 01_layout.css
        - <body>의 전체에 배달의 민족 주아체를 적용시켰고, header의 텍스트의 경우에 gugi체를 적용함
        - header의 경우 백그라운드 이미지를 적용했고 사이즈를 명세서에 따라 고정함. footer의 경우 백그라운드 컬러를 적용했고 사이즈를 고정함.

    - 02_movie.html
        - Grid layout을 적용시키기 위해 container 클래스를 이용함
        - 영화 목록 페이지를 만들어 카드 형태로 6개의 영화를 정렬함. 이때, 디바이스의 가로 픽셀 크기에 따라서 한줄에 정렬되는 카드의 수가 바뀌게 되는데 이것을 반응형이라함
        - 각 카드는 영화포스터, 영화명, 평점, 장르, 개봉일, 영화 상세정보 url 버튼을 포함

    - 02_movie.css : 01_layout.css와 동일

	- 03_detail_view.html
		- 영화 목록 카드의 포스터 이미지를 클릭시 영화 상세보기 기능 추가 (Modal 활용)
		- 영화 상세보기 Modal 팝업은 영화의 이미지 3장, 연령등급, 누적 관객수, 줄거리를 포함
		- 영화의 이미지 3장의 경우 carousel을 활용하여 옆으로 넘기면서 볼 수 있음
	
	- 03_detail_view.css: 01_layout.css와 동일

    - assets/ : header의 백그라운드 이미지, 영화 포스터, 영화 이미지, Top 버튼 이미지, favicon 이미지, Navbar의 제목 이미지를 포함한 프로젝트를 위한 이미지 폴더