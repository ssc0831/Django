import pandas as pd

# year  sales
# 2018  350
# 2019  400
# 2020  1050
# 2021  2000
# 2022  1000
data_dic = {
    'year' : [2018, 2019, 2020, 2021, 2022],
    'sales' : [350, 400, 1050, 2000, 1000]
}

print(data_dic)
print(type(data_dic))

df = pd.DataFrame(data_dic)
print(df)
print(type(df))

print('='*20)

df2 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]],
index=['중간고사', '기말고사'],
columns=['1반', '2반', '3반'])
print(df2)

df3 = pd.DataFrame([[20201101, 'Kim', 90, 95], [20201102, 'Lee', 80, 85],
                    [20201103, 'Hong', 70, 75], [20201104, 'Park', 60, 95]],
                    columns=['학번', '이름', '중간고사', '기말고사']
                    )
print(df3)
print('df3 중간고사 합계 : ', df3['중간고사'].sum())
print('df3 기말고사 합계 : ', df3.기말고사.sum())
df3['총점'] = df3.중간고사 + df3.기말고사
# df3.'총점' = df3.중간고사 + df3.기말고사
# 새로운 컬럼 생성할때는 . 사용 못 함
print(df3)
print('\n', df3.sum())
# print('\n', df3.mean()) - 오류
print('시험 평균' , df3.총점.mean())
print('*'*20)
df4 = pd.DataFrame([[20201101, 'Kim', 90, 95], [20201102, 'Lee', 80, 85],
                    [20201103, 'Hong', 70, 75], [20201104, 'Park', 60, 95]],
                    )
print(df4)
df4.columns = ['학번', '이름', '중간고사', '기말고사']
print(df4)
print(df4.tail())

# 파일 보내기
df3.to_csv('pandas2.csv', header='False')

# 파일 읽기
df5 = pd.read_csv('pandas2.csv', encoding='utf-8')
print(df5)