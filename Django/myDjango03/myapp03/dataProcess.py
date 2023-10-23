import re
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def make_wordCloud(data):
    # Regular Expression(정규표현식)
    # ^은 시작을 의미 []에서 사용하면 제외
    # [0-9]가 숫자인 패턴을 찾는 것이라면, [^0-9]는 숫자인 패턴을 제외한다는 뜻
    # s = '좋은 아침이예요. 안녕하세요'
    # m = re.sub('^안녕', s)

    # print(data)

    message = ''
    for item in data:
        if 'message' in item.keys():
            message = message + re.sub(r'[^\w]',' ', item['message'])+''
    nlp = Okt()
    message_N = nlp.nouns(message)  # 명사 추출
    count = Counter(message_N)
    word_count = dict()
    for tag, counts in count.most_common(80):
        print("%s : %d" %(tag))
        if(len(str(tag)) > 1):
            print("%s : %d" %(tag, counts))
    
        font_path = 'C:/Windows/font/malgun.ttf/'
        wc = WordCloud(font_path, background_color='ivory', width=800, height=600)
        cloud = wc.generate_from_frequencies()
        plt.figure(figsize=(0,0))
        plt.imshow(cloud)
        plt.axis('off')
        cloud.to_file('./static/images/k_wordCloud.png')
    return