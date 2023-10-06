import requests
from bs4 import BeautifulSoup
import re

header = {'User-Agent' : 'Mozilla/5.0'}
req = requests.get('https://www.melon.com/chart/index.htm', headers=header)
soup = BeautifulSoup(req.text, 'html.parser')
# print(soup)
# BeautifulSoup으로 사용시 Celenium으로 할 때 Request 200이 떠서 되는 것이
# 아무것도 뜨지 않기 때문에 헤더의 접속정보를 추가하여 알려줘야 함.

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
    # like = tr.select_one('#lst50 > td:nth-child(8) > div > button > span.cnt').get_text()
    # like = re.sub('\n총건수\n', '', like) # 정적인 크롤링으로는 좋아요가 0이 나오므로 구하기가 불가
    # like = re.sub(',','', like)
    # print(like)
    datas.append([rank, name, singer, album])
print(datas)