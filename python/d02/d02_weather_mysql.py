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

select_weather = "select tmef from forecast order by tmef desc limit 1"
cur = conn.cursor()
cur.execute(select_weather)

last_data = cur.fetchone() # DB에 있는 최신 날짜
print(last_data)
print(type(last_data))

# print(soup.find_all('location'))
weather = {}
for i in soup.find_all('location') :
    weather[i.find('city').text] = []
    for j in i.find_all('data'):
        temp = []
        # if (len(last_data)==0) or (j.find('tmef').text > last_data[0]['tmef']):
        if (last_data is None) or (str(last_data[0]) < j.find('tmef').text ):
            temp.append(j.find('tmef').text)
            temp.append(j.find('wf').text)
            temp.append(j.find('tmn').text)
            temp.append(j.find('tmx').text)
            weather[i.find('city').string].append(temp)
            # print(temp)
# print(weather)   

for i in weather:
    for j in weather[i]:
        cur = conn.cursor()
        cur.execute(insert_weather, (i, j[0],j[1],j[2],j[3]))
        conn.commit()