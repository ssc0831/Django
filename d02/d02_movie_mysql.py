from bs4 import BeautifulSoup
import requests
import pymysql

# DB 연결
# pip install pymysql - MySQL Python 연동되도록 패키지 설치 먼저 해주세요.
dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "root"

conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser, passwd=dbPass,
                       db='bigdb', charset='utf8', use_unicode=True)
insert_sql = "insert into daum_movie(title, grade, reserve) value(%s, %s, %s)"

req = requests.get('https://movie.daum.net/ranking/reservation')

html = req.text
soup = BeautifulSoup(html, 'html.parser')

ols = soup.find('ol', class_='list_movieranking')
rankcount = ols.find_all('div', class_ ='thumb_cont')

# DB CRUD
# 1. insert
cur = conn.cursor() # conn.cursor()는 SQL 쿼리를 실행하고 결과를 조회
for i in rankcount:
    moviename = i.find('a', class_='link_txt').get_text()
    moviegrade = i.find('span', 'txt_grade').get_text()
    movieReser = i.find('span', {'class' : 'txt_num'}).get_text()
    cur.execute(insert_sql,(moviename, moviegrade, movieReser))
    conn.commit()