import pymysql
import matplotlib as mpl
import matplotlib.pyplot as plt

# DB 연결
# DB를 불러 평점을 나타내기
dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "root"

conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser, passwd=dbPass,
                       db='bigdb', charset='utf8', use_unicode=True)

# Select
select_sql = "select grade from daum_movie"

cur = conn.cursor()
cur.execute(select_sql)
movies = cur.fetchall()
# print(movies)
# print(type(movies)) # 자료형이 Tuple 형태로 나타남

# 평점이 9점이상, 8점이상, 6점이상, 6점미만을 Pie Chart로 그리기(pyplot 활용)
movieDic = {'9.0이상':0, '8.0이상':0, '6.0이상':0, '6.0미만':0}

for movie in movies:
    movie = float(movie[0])
    # print(movie)
    if movie >= 9:
        movieDic['9.0이상'] +=1
    elif movie >= 8:
        movieDic['8.0이상'] +=1
    elif movie >= 6:
        movieDic['6.0이상'] +=1
    else:
        movieDic['6.0미만'] +=1
print(movieDic)

# 한글처리
font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

figure = plt.figure()
axes = figure.add_subplot(111)
axes.pie(movieDic.values(), labels=movieDic.keys(), autopct='%.1f%%')
plt.show()