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
y = set(re.findall(char, script101))
print(type(y))
print('='*30)

# set형태를 list로 전환
z = list(y)
print(type(z))
print(z)

for i in z:
    print(i[:-1]) # :(콜론) 부분 제외 호출


character = []
for i in z:
    character += [i[:-1]]
print(character)

print('='*30)
character2 = []
for i in z:
    char = re.sub(':', '' ,i)
    # print(char, end= ' ')
    character2.append(char)
print(character2)
#################
print()
print('='*20)
print(script101)
#################
ch = 'Scene:'
ch = re.sub(':','',ch)
print(ch)
#################
a = '제 이메일 주소는 greate@naver.com'
a += ' 오늘은 today@naver.com 내일은 apple@gmail.com life@abc.co.kr라는 메일을 사용합니다.'
print(a)
# E-mail의 주소값만 출력(greate@naver.com, today@naver.com, apple@naver.com, life@abc.co.kr)
a1 = re.findall(r'[a-z]+@[a-z.]+',a)
print(a1)
################
words = ['apple', 'cat', 'brave', 'drama', 'asise', 'blow', 'coat', 'above']
mm = []
for i in words :
    mm += re.findall(r'a[a-z]+', i)
print(mm)
print()

for i in words :
    m = re.search(r'a[a-z]+', i)
    if m:
        print(m.group())
print()
for i in words :
    # m = re.match(r'a[a-z]+', i) # match는 시작위치에서 패턴을 찾음
    m = re.match(r'a\D+', i) # \d(숫자) \D(숫자가 아닌)
    if m:
        print(">>>>", m.group())

