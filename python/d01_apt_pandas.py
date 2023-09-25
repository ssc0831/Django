# apt_201910.csv 읽어오기

import pandas as pd

df = pd.read_csv('apt_201910.csv', encoding='cp949') # 인코딩 없으면 오류남
print(len(df))
print(df.shape)
print(df.head())
print(df.tail())