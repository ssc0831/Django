from selenium import webdriver as wd
from bs4 import BeautifulSoup

driver = wd.Chrome()
driver.get('https://www.melon.com/chart/index.htm')

page = driver.page_source
# print(page) # 페이지의 소스 찍기
soup = BeautifulSoup(page, 'html.parser')
