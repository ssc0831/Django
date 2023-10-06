from selenium import webdriver as wd
from bs4 import BeautifulSoup
import re

driver = wd.Chrome()
driver.get('https://www.melon.com/chart/index.htm')

page = driver.page_source
# print(page) # 페이지의 소스 찍기
soup = BeautifulSoup(page, 'html.parser')

# 접속하고자 하는 사이트 뒤에 /robots.txt를 붙여주면 사이트에서 접근 가능한 영역 확인할 수 있음.
# 예시> https://www.naver.com/robots.txt 같이 사용하면 됨.
# 접근 불가능한 영역도 있기 때문에 모든 정보들을 크롤링을 할 수는 없다.

#frm > div > table > tbody
tbody = soup.select_one('#frm > div > table > tbody')
#lst50
trs = tbody.select('tr#lst50')

datas = []
# ['1', 'Love Lee', 'AKMU(악뮤)', 'Love Lee', '87738'] , ...
for tr in trs:
    rank = tr.select_one('span.rank').get_text()
    
    #lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a
    name = tr.select_one('div.ellipsis.rank01 > span > a').get_text()
    
    #lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a
    singer = tr.select_one('div.ellipsis.rank02 > a').get_text()
    
    #lst50 > td:nth-child(7) > div > div > div > a
    album = tr.select_one('div.rank03 > a').get_text()
    
    #lst50 > td:nth-child(8) > div > button > span.cnt
    like = tr.select_one('span.cnt').get_text()
    like = re.sub('\n총건수\n', '', like)
    like = re.sub(',','', like)
    # print(like)
    datas.append([rank, name, singer, album, like])
print(datas)

# melon.csv 순위, 곡명, 가수, 앨범, 좋아요 \n
with open('melon.csv', 'w', encoding='utf-8-sig') as file:
    file.write('순위, 곡명, 가수, 앨범, 좋아요\n')
    for item in datas:
        row = ', '.join(item)
        file.write(row+"\n")



