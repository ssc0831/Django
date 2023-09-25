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

# 단지명, 가격 출력 면적이 130㎡ 초과인 것만 출력하기
print(df.loc[: , ['단지명', '가격', '면적']][df.면적 > 130])

print('-'*20)
# 지역에 강릉이 들어간 자료만 출력
local_area = df[df.시군구.str.find('강릉') > -1]
print(local_area)
# 지역이 강릉인 시군구, 가격, 면적 10행 출력하기
print(local_area.loc[:10, ['시군구', '가격', '면적']])
print(local_area.loc[:10, ('시군구', '가격', '면적')])

print('-'*20)
# 가격만 5행 출력하기
print(df['가격'].head())
# 면적이 130㎡ 넘는 아파트 가격
print(df.가격[df.면적 > 130])