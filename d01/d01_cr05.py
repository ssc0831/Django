import requests
from bs4 import BeautifulSoup

res = requests.get('https://m.dhlottery.co.kr/gameResult.do?method=byWin')
soup = BeautifulSoup(res.content, 'html.parser')
# ballNum = soup.find_all('span', 'ball')
ballNum = soup.find_all('span', class_ = "ball")
# print(ballNum)
for i in ballNum:
    print(i.get_text(), end='\t')
print('\n-----------------------')
# "#container > div > div.bx_lotto_winnum > span:nth-child(1)"
nums = soup.select('#container > div > div.bx_lotto_winnum > span.ball')
# print(nums)
for i in nums:
    print(i.string, end='\t')