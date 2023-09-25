from bs4 import BeautifulSoup

html = """
    <html><body>
    <h1>스크레이핑이란</h1>
    <p>웹 페이지를 분석하는 것</p>
    <p>원하는 부분을 추출하는 것</p>
    </body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
print(soup)
h1 = soup.html.body.h1
print(h1)
p = soup.html.body.p
print(p)
p1 = p.next_sibling.next_sibling # next_sibling : 형제의 요소 찾기(html 파싱에 사용)
print(p1)
print("h1 :", h1.string)
print("p :", p.string)
print("p1 :", p1.string)
