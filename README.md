# Python Django
## 데이터 시각화(Data Visualization)를 위한 Python & Django
### d01 Python Library
#### pandas, re(정규 표현식(Regular Expression))활용, 웹 크롤링
- pandas, re, bs4(BeautifulSoup) & request 활용
- import pandas, import re, from bs4 import BeautifulSoup, import requests 사용
- 패키지 설치 안되있을때는 pip install 사용하여 패키지 설치해줘야 한다.

### d02 Python Library
#### 웹 크롤링(정적 크롤링, 동적 크롤링)
- bs4(BeautifulSoup) & request 활용, pandas로 파일 읽기 및 내보내기, matplotlib 활용하기
- 웹 크롤링 개념 복습, 영화 평점 가져오기, 날씨 알아내기 및 matplot 활용하여 차트 만들기(결과값은 따로 폴더 저장함)
- 동적 크롤링(Selenium 패키지 활용)
- pip install selenium -> 패키지 설치
- https://chromedriver.chromium.org/downloads 활용하여 해줘야 함.
- https://googlechromelabs.github.io/chrome-for-testing/ -> Stable 버전 다운로드 들어가서 Chrome Driver를 설치

#### 웹 크롤링 DB 연동
- 웹 크롤링 SQL연동(MySQL 활용)
- pip install pymysql (MySQL을 Python에서 사용에 필요한 라이브러리) -> 패키지 설치
- bigdb Schema 생성, daum_movie, forecast Table 생성
- DB 연결 및 DB 삽입, 선택 작업
- PieChart 그리기(matplotlib 활용)
- pip install lxml (xml 파싱 라이브러리) -> 패키지 설치

### d03 Python Library
#### 웹 크롤링 DB 연동 d02것 이어서
- 날씨 정보 추출, 날짜별 최고기온, 최저기온 출력
- WordCloud 활용