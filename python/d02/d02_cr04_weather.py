import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv('weather44.csv', index_col='point', encoding='euc-kr')
print(df)

# 서울, 인천, 대전, 대구, 광주, 부산, 울산 지역만 읽어들이기
# print(df.loc[['서울', '인천']]) - 서울과 인천만 출력
city_df = df.loc[['서울', '인천', '대전', '대구', '광주', '부산', '울산']]
print(city_df)

# Graph 그리기
# 한글
font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

# 차트의 종류, 제목, 차트크기, 범례, 폰트 크기
ax = city_df.plot(kind='bar', title='날씨', figsize=(12,7), legend=True, fontsize=12)
ax.set_xlabel('도시')
ax.set_ylabel('기온/습도')
ax.legend(['기온', '습도'])
plt.show()