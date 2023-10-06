import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

res = requests.get('https://finance.naver.com/')
soup = BeautifulSoup(res.content, 'html.parser')

# "#container > div.aside > div > div.aside_area.aside_popular > table > tbody"
tbody = soup.select_one("#container > div.aside > div > div.aside_area.aside_popular > table > tbody")
# print(tbody)
trs = tbody.select('tr')
# print(trs)
datas = []
for i in trs:
    name = i.select_one('th > a').get_text()
    curr_price = i.select_one('td').get_text()
    # ch_direction = i['class'][0]
    ch_direction = i.select_one('td > img')['alt']
    # ch_direction = i.select_one('td > em > span').get_text()
    ch_price = i.select_one('td > span').get_text().strip()
    datas.append([name, curr_price, ch_direction, ch_price])
# print(name)
print(datas)
print('\n---------------------------------------')

# Workbook 활용하여 Spread Sheet(xlsx) 파일 만들기
# write_wb = Workbook()
# write_ws = write_wb.create_sheet('결과')
# for data in datas:
#     write_ws.append(data)

# write_wb.save(r'testfinace.xlsx')
