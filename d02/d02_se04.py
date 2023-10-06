from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
r = driver.execute_script('return 1000*50') # Selenium WebDriver에서 JavaScript 코드를 실행하기 위해 사용
print(r) # Selenium 열리면서 50000이 출력됨