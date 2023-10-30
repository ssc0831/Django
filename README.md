# Python Django
## 데이터 시각화(Data Visualization)를 위한 Python & Django
## Python
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
- pip install WordCloud
- WordCloud 활용

## Django(장고)
### Django 활용
- pip install django - Django 설치(오류가 나면 관리자모드로 설치해주세요.)
- pip install mysqlclient – Django에서 DB(MySQL)연결을 하기 위한 설치

### 프로젝트 생성
- django-admin startproject [project명]
- 예시> django-admin startproject myDjango01
- myDjango01로 이동

### 프로젝트 앱 실행 및 구동
- python manage.py startapp myapp01
- python manage.py makemigrations, python manage.py migrate(마이그레이션)
- python manage.py runserver(서버 구동)
- url.py, models.py, html(write.html, detail.html, detail1.html), views.py 수정 및 만들기
- 파일 업로드하기(REST API 활용)

### 파일 업로드
- 파일 업로드 이어서
- {% load static %} => Bootstrap, JQuery 등 로컬 파일 불러들이는 문법, 첫줄에 적어준다.
- {% if board.filesize > 0 %}~{% endif %} 문법
- from django.http.response import JsonResponse(JSON 객체 불러오기)
- 삭제, 댓글추가, 게시판, 검색설정
- Q객체 (from django.db.models import Q) Django에서 SQL을 처리할 때 WHERE AND, OR, NOT의 필터링을 정의하는 연산자로 사용
- import math(반올림, 버림 사용)

### HTML5에서의 Header, Body, Footer를 활용한 방식의 Django 구축
- STATICFILES_DIRS, BASE_DIR 이용하여 경로 잡기
- {% block content %}, {% endblock %}, {% block script %}, {% endblock %}

### Django 활용(ORM 기반)
- 회원가입 폼 활용하기(django.contrib.auth 활용)
- 유효성검사
- 페이징
- python manage.py createsuperuser 슈퍼유저 만들기
- pip install konlpy (한국어 자연어 처리를 위한 라이브러리(한글 형태소 분석 라이브러리) - JRE 필요)
- {% get_static_prefix %} static을 참조하여 파일을 가져올 때 사용
- pip install pytagcloud (단어 클라우드 만드는 라이브러리)
- pip install pygame (프로토타이핑 라이브러리)
- pip install simplejson(JSON 데이터 다루는 라이브러리)
- 폴더(C:\Python\Python311\Lib\site-packages\pytagcloud\fonts)에 폰트 다운로드해서 폰트 삽입하기(네이버 마루부리 폰트)

### Django 활용
- melon chart 1~10위까지 뽑아보기
- pip install folium
- folium 활용 지도 띄우기
- TEMPLATE_DIR = os.path.join(BASE_DIR, 'myapp03/templates') 경로지정 추가
- import os
- from myDjango03.settings import TEMPLATE_DIR 추가
- Pandas(groupby) (pandas에서 groupby는 데이터를 특정 기준으로 그룹화하여 분석하는 기능이다.)

- font_manager(Python의 기본 폰트 관리 모듈)
- rc(Python의 설정 파일, Python 프로그램의 기본 설정을 지정)
- annotate는 QuerySet에 추가적인 필드를 추가하는 기능이다.
- django.db.models.aggregates 쿼리셋 집계 모듈이다.(다양한 집계 함수를 제공)
