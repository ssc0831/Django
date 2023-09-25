# apt_201910.csv 읽어오기

import pandas as pd

df = pd.read_csv('apt_201910.csv', encoding='cp949') # 인코딩 없으면 오류남
print(len(df))
print(df.shape)
print(df.head())
print(df.tail())
print('-'*20)

# 면적이 200㎡보다 큰 것 출력
print(df['면적'])
print(df[df.면적 > 200])
print('-'*20)

# 단지명, 가격 10개 출력 - loc 사용
print(df.loc[:10, ['단지명', '가격']])