import re
import codecs

f = codecs.open('friends101.txt', 'r', encoding='utf-8')
script101 = f.read()

print(script101[:100])
Line = re.findall(r'Monica:.+',script101)
print(Line)
print('-'*20)
print(Line[:3])
print(type(Line))

All = re.findall(r'All:.+', script101)
print(All)
print(All[-1])
print(len(All))
print('-'*20)

char = re.compile(r'[A-Z][a-z]+:')
print(re.findall(char, script101))

a = [1, 2, 3, 4, 5, 2, 2]
print(a)
print(set(a)) # set은 값의 중복 허용 하지 않는 자료 구조

print(set(re.findall(char, script101)))