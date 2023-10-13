import pymysql
import matplotlib.pyplot as plt
import matplotlib as mpl

dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "root"

conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser, passwd=dbPass,
                       db='bigdb', charset='utf8', use_unicode=True)

font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

select_data = "select * from forecast where city = '부산'"
curr = conn.cursor()
curr.execute(select_data)
result = curr.fetchall()
# print(result)

# 날짜, 최고기온, 최저기온
low = [] # 최저기온
high = [] # 최고기온
xdata = [] # 날짜
for r in result:
    low.append(int(r[4])) # 자료형 변환(캐스팅)
    high.append(int(r[5])) # 자료형 변환(캐스팅)
    xdata.append(r[2])

plt.figure(figsize=(10,6))
plt.plot(xdata, low, label='최저기온')
plt.plot(xdata, high, label='최고기온')
plt.title('부산 기온')
plt.legend()
plt.show()

# 부산의 구름 많음, 맑음 날씨의 빈도 나타내기
select_data1 = "select wf, count(*) from forecast where city='부산' group by wf"
curr.execute(select_data1)
result1 = curr.fetchall()
print(result1)

wfData = []
wfCount = []
for r in result1:
    wfData.append(r[0])
    wfCount.append(r[1])
plt.bar(wfData, wfCount)
plt.show()

# PieChart로 그리기
plt.pie(wfCount, labels=wfData, autopct='%.1f%%')
plt.show()