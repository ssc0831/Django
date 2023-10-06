from bs4 import BeautifulSoup
import requests

# 제목 평점 예매율 가져오기
req = requests.get('https://movie.daum.net/ranking/reservation')
# print(req) # <Response [200]> - 정상적으로 Response가 되었다고 출력됨.
# print(req.text)를 하게 되면 html 태그 출력가 출력이 됨.

html = req.text
soup = BeautifulSoup(html, 'html.parser')

#mainContent > div > div.box_ranking > ol > li:nth-child(1) > div > div.thumb_cont > strong
#mainContent > div > div.box_ranking > ol

# ols = soup.find('ol', class_='list_movieranking')
# rankcount = ols.find_all('div', class_ ='thumb_cont')
# print(rankcount)

ols = soup.select_one('#mainContent > div > div.box_ranking > ol')
rankcount = ols.select('li')
# rankcount = ols.select('div.thumb_cont')
print(rankcount)

for i in rankcount:
    moviename = i.find('a', class_='link_txt').get_text()
    moviegrade = i.find('span', 'txt_grade').get_text()
    movieReser = i.find('span', {'class' : 'txt_num'}).get_text()
    print('영화 : ', moviename, end=' / ')
    print('평점 : ', moviegrade, end=' / ')
    print('예매율 : ', movieReser)

print('-'*20)
for i in rankcount:
    moviename = i.select_one('a.link_txt').get_text()
    moviegrade = i.select_one('span.txt_grade').get_text()
    movieReser = i.select_one('span.txt_num').get_text()
    print('영화 : ', moviename, end=' / ')
    print('평점 : ', moviegrade, end=' / ')
    print('예매율 : ', movieReser)