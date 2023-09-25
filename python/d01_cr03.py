import requests # pip install requests로 패키지 설치
from bs4 import BeautifulSoup

res = requests.get('http://media.daum.net/digital/')
# print(res.content)
soup = BeautifulSoup(res.content, 'html.parser')
print(soup)
link_title = soup.find_all('a', 'link_txt')
# print(link_title)
for i in link_title:
    print(i.get_text().strip())