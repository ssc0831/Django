from bs4 import BeautifulSoup
import requests
import pandas as pd

req = requests.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')
soup = BeautifulSoup(req.text, 'html.parser')

#weather_table > tbody
tbody = soup.select_one('#weather_table > tbody')
# print(tbody)
datas = []
for tr in tbody.select('tr'):
    tds = tr.select('td')
    # print('지역 = ', tds[0].text)
    # print('온도 = ', tds[5].text)
    # print('습도 = ', tds[-4].text)
    # print()
    datas.append([tds[0].text, tds[5].text, tds[-4].text])
# print(datas)

# for item in datas:
#     print('item = ', item)

# Python 내장 라이브러리로 파일 보내는 방법
# with open('weather33.csv', 'w') as file:
#     print('파일저장')
#     file.write('point, temp, hum \n')
#     for item in datas:
#         row = ','.join(item)
#         file.write(row+'\n')

# Pandas로 CSV파일 읽기
df = pd.read_csv('weather33.csv', encoding='euc-kr')
print(df)

# Pandas로 CSV파일 내보내기
# df1 = pd.DataFrame(datas, columns=('point', 'temp', 'hum'))
# df1.to_csv('weather44.csv', encoding='euc-kr', index=False)

print("-"*20)
df = pd.read_csv('weather44.csv', encoding='euc-kr')
print(df)
