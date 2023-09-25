import requests
from bs4 import BeautifulSoup
import re

res = requests.get('https://finance.naver.com/')
soup = BeautifulSoup(res.content, 'html.parser')
selected_elements1 = soup.select("#container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr")
selected_elements2 = soup.select("#container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr > td > em > span")

selected_elements = selected_elements1 + selected_elements2

for element in selected_elements:
    print(element.get_text())

print('\n---------------------------------------')

# "#container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr:nth-child(1)"
# "#container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr:nth-child(1) > td:nth-child(3) > em > span"