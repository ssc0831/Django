from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import re
import pandas as pd

driver = wd.Chrome()
driver.implicitly_wait(2)
# 데이터를 받는동안 크롤링하면 오류가 나기에 이같이 시간을 두고 크롤링 해야 함.
# 웹 페이지가 로딩되는 시간이나 AJAX 요청과 같이 동적으로 내용이 변경되는 경우
# 요소가 즉시 나타나지 않더라도 일정 시간 동안 기다림으로써 요소가 나타날 때까지 기다리는 시간 설정이
# driver.implicitly_wait 이다.
driver.get('https://www.melon.com/chart/index.htm')

# //*[@id="frm"]/div/table/tbody
tbody = driver.find_element(By.XPATH, '//*[@id="frm"]/div/table/tbody')
trs = tbody.find_elements(By.TAG_NAME, 'tr')

datas = []

for tr in trs:
    rank = tr.find_element(By.CLASS_NAME, 'rank').text
    title = tr.find_element(By.CLASS_NAME, 'wrap_song_info').find_element(By.TAG_NAME,'a').text
    singer = tr.find_element(By.CSS_SELECTOR, 'div.ellipsis.rank02').find_element(By.TAG_NAME,'a').text
    album = tr.find_element(By.CSS_SELECTOR, 'div.rank03').find_element(By.TAG_NAME,'a').text
    like = tr.find_element(By.CLASS_NAME, 'like').find_element(By.CLASS_NAME,'cnt').text
    like = re.sub(',','',like)
    datas.append([rank, title, singer, album, like])

print(datas)
# Pandas로 CSV 파일 보내기
# df1 = pd.DataFrame(datas, columns=('순위', '제목', '가수', '앨범', '좋아요 수'))
# df1.to_csv('melon33.csv', encoding='utf-8-sig', index=False)