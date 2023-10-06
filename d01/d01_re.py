import re

text = "<title>지금은 문자열 연습입니다.</title>"
print(text[0:7]) #print(text[:7])
print(text.find('문')) # 값이 있을 때 위치값을 리턴
print(text.find('파')) # 값이 없을 때는 -1 리턴
print(text.index('문')) # 있으면 위치 값 리턴
# print(text.index('파')) # 없을 때는 오류 발생

text1 = "    <title>지금은 문자열 연습입니다.</title>    "
text2 = ";"
print(text1.strip()+text2)
print(text1.lstrip()+text2) # 왼쪽 공백만 제거
print(text1.rstrip()+text2) # 오른쪽 공백만 제거
print(text1.replace('<title>','<div>'))
print(text1.replace('<title>',''))

text3 = ('111<head>안녕하세요</head>22')
body = re.search('<head.*/head>', text3)
print(body)
body = body.group() # 원하는 데이터 출력할 때 사용
print(body)

# 정규 표현식(Regular Expression)
# [0-9] 숫자 [a-z] 소문자 [A-Z] 대문자
# ab*c : 0이상을 의미(abc, abbc, abbc, abbbbbbbbc, ...)
# * 0이상, + 1 이상, ? 0이상 1이하 
print('='*20)
text4 = ('<head>안녕하세요...<title>지금은 문자열 출력 연습</title></head>')
# <title>지금은 문자열 연습</title> 출력
body = re.search('<title.*/title>', text4)
body = body.group()
print(body) # body : <title>지금은 문자열 출력 연습</title>
print('#####')
print(re.search('<.+?>', body).group()) # <title>만 나옴
print(re.search('<.+?>', text4).group()) # <head>만 나옴
print('#####')
body = re.sub('<.+?>','',body) # 지금은 문자열 출력 연습만 출력이 됨.
print(body)