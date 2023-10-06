from bs4 import BeautifulSoup
import requests
import pymysql

# DB 연결
dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "root"

conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser, passwd=dbPass,
                       db='bigdb', charset='utf8', use_unicode=True)
insert_weather = "insert into forecast(city, tmef, wf, tmn, tmx) value(%s, %s, %s, %s,%s)"
req = requests.get('https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108')
html = req.text

# pip install lxml - lxml Parsing 패키지 설치
soup = BeautifulSoup(html, 'lxml')
print(soup)
