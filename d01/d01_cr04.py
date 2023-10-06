import requests
from bs4 import BeautifulSoup
import re

res = requests.get('http://news.daum.net/economic/')
soup = BeautifulSoup(res.content, 'html.parser')
# print(soup)
links = soup.select('a[href]')
# print(links)
for i in links:
    if re.search('https://v.\w+', i['href']): # .은 임의의 문자 1개, \w 숫자와 문자
        print(i.get_text().strip())