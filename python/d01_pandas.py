import pandas as pd # pip install pandas로 패키지 설치

# numpy : 수치 데이터를 다루기 위한 라이브러리
# pandas : 데이터 분석에 자주 사용하는 테이블형태 다루는 라이브러리
    # 1차원 자료구조 : Series
    # 2차원 자료구조 : DataFrame(많이 사용하는 데이터 구조)
    # 3차원 자료구조 : Panel

# List [], Tuple () - 한번 자료 지정하면 수정불가,
# Dictionary {}
data = {
    'name': ['Mark', 'Jane', 'aaa', 'rr'],
    'age': [33, 44, 55, 11],
    'score': [91.2, 88.5, 55.6, 88.9]
}

# print(data)

df = pd.DataFrame(data)
print(df)
print(type(df))
print(df.sum())
print(df.age.mean()) #print(df['age'].mean())
print(df.age)