# 동적 크롤링하기
# pip install selenium으로 selenium 먼저 설치하고 진행하기

from selenium import webdriver as wd
from selenium.webdriver.common.by import By

driver = wd.Chrome()
driver.get('https://naver.com')
# DevTools listening on ws://127.0.0.1:52836/devtools/browser/32d488ed-4c2e-4037-becb-434de55b079a 같이 뜬다.
# 곧 바로 닫히지만 Driver가 정상적으로 뜬 것이다.

# 검색창에 파이썬 입력하고 결과 값 크롤링하기
driver.find_element(By.ID, 'query').send_keys('파이썬')
driver.find_element(By.CLASS_NAME, 'btn_search').click()