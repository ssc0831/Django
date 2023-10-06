from selenium import webdriver as wd
from bs4 import BeautifulSoup

driver = wd.Chrome()
driver.get('https://www.melon.com/chart/index.htm')

# 페이지의 소스 찍기
page = driver.page_source
# print(page)
soup = BeautifulSoup(page, 'html.parser')
