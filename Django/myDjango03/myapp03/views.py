from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from myapp03.models import Board, Comment, Movie
from .form import UserForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models.aggregates import Count, Avg
import json
from myapp03 import dataProcess
import math
import pandas as pd

# Create your views here.

UPLOAD_DIR = 'C:/Django_Works/upload/'

# Melon
def melon(request):
   # 순위 곡명 가수 앨범
   datas = []
   dataProcess.melon_crawling(datas)
   # return render(request, "bigdata/melon.html", {'data': datas})
   return render(request, "bigdata/melon1.html", {'data': datas})

# Map
def map(request):
   dataProcess.map()
   return render(request, 'bigdata/map.html')

# MovieChart
def movie_chart(request):
   data = []
   dataProcess.movie_crawling(data)
   # print(data)
   df = pd.DataFrame(data, columns=['제목', '평점', '예매율'])
   # print(df)
   group_title = df.groupby('제목')
   print(group_title)
   # 제목별 그룹화해서 평점의 평균 구하기
   group_mean = df.groupby('제목')['평점'].mean().sort_values(ascending=False).head(10)
   # print(group_mean)
   df1 = pd.DataFrame(group_mean, columns=['평점'])
   print(df1)
   dataProcess.movie_daum_chart(df1.index, df1.평점)

   return render(request, 'bigdata/movie_daum.html',
                 {'img_data' : 'movie_daum_fig.png'})

# Movie => 테이블 insert
def movie(request):
   data = []
   dataProcess.movie_crawling(data) # 이미 movie_crawling을 만들었기 때문에 따로 안 만들어도 됨
   # data가 들어 있는 순서 : title, point, reserve
   for r in data:
      movie = Movie(title = r[0], point = r[1], reserve = r[2])
      movie.save()
   return redirect('/')

# Movie DB Chart
def movie_dbchart(request):
   # movie 테이블에서 제목(title)에 해당하는 평점(point) 평균을 구하기
   data = Movie.objects.values('title').annotate(point_avg=Avg('point')).order_by('-point_avg')[0:10]
   # print('data query : ', data.query)
   df = pd.DataFrame(data)
   # print('data query : ', df)
   print('df : ', df)
   dataProcess.movie_chart(df.title, df.point_avg)
   return render(request, 'bigdata/movie.html',
                 {'img_data' : 'movie_fig.png'},
                 {'data' : data})

# WordCloud
def wordcloud(request):
   a_path = 'C:/Django_Works/Django/myDjango03/data/'
   data = json.loads(open(a_path+'4차 산업혁명.json', 'r',
                          encoding='utf-8').read())
   dataProcess.make_wordCloud(data)
   return render(request, 'bigdata/word.html',
                 {'img_data' : 'k_wordCloud.png'})

def wordcloud2(request):
   a_path = 'C:/Django_Works/Django/myDjango03/data/'
   data = json.loads(open(a_path+'4차 산업혁명.json', 'r',
                          encoding='utf-8').read())
   dataProcess.make_wordCloud2(data)
   return render(request, 'bigdata/word.html',
                 {'img_data' : 'pytag_word.png'})

# signup
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('/')
        else:
           print("signup POST un_valid'")     
    else:
        form = UserForm()

    return render(request, 'common/signup.html', {'form' :form })


#######################
# write_form
@login_required(login_url='/login')
def write_form(request):
    return render(request, 'board/insert.html')

# insert
@csrf_exempt
def insert(request):
    fname=''
    fsize=0

    if 'file' in request.FILES:
        file = request.FILES['file']
        fname = file.name
        fsize = file.size
        
        fp = open('%s%s' %(UPLOAD_DIR, fname),'wb')
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()  
    
    board = Board(writer = request.user,
                  title = request.POST['title'],
                  content = request.POST['content'],
                  filename = fname,
                  filesize = fsize )
    board.save()
    return redirect('/list')


# list
def list(request):
  page = request.GET.get('page', 1)
  field = request.GET.get('field', 'title')
  word = request.GET.get('word', '')

  # count
  if field == 'all':
     boardCount = Board.objects.filter(
        Q(writer__contains = word)|
        Q(title__contains=word) |
        Q(content__contains=word)).count()
  elif field =='writer':
     boardCount = Board.objects.filter(
        Q(writer__contains = word)).count()

  elif field =='title':
     boardCount = Board.objects.filter(
        Q(title__contains = word)).count()
     
  elif field =='content':
      boardCount = Board.objects.filter(
        Q(content__contains = word)).count()

  else:
     boardCount = Board.objects.all().count()


  pageSize =5
  blockPage =3
  currentPage = int(page)
  start = (currentPage-1) * pageSize
  ## 123[다음]   [이전]456[다음]  [이전]789[다음]
  totPage = math.ceil(boardCount/pageSize)  # 7
  startPage = math.floor((currentPage-1)/blockPage)*blockPage+1
  endPage = startPage+ blockPage -1
  if  endPage >  totPage:
     endPage = totPage

  # 내용
  if field == 'all':
     boardList = Board.objects.filter(
        Q(writer__contains = word)|
        Q(title__contains=word) |
        Q(content__contains=word)).order_by('-id')[start:start+pageSize]
  elif field =='writer':
     boardList = Board.objects.filter(
        Q(writer__contains = word)).order_by('-id')[start:start+pageSize]

  elif field =='title':
     boardList = Board.objects.filter(
        Q(title__contains = word)).order_by('-id')[start:start+pageSize]
     
  elif field =='content':
      boardList = Board.objects.filter(
        Q(content__contains = word)).order_by('-id')[start:start+pageSize]

  else:
     boardList = Board.objects.all().order_by('-id')[start:start+pageSize]

  context = {'boardList' : boardList,
             'boardCount' : boardCount,
             'startPage' : startPage,
             'blockPage' :blockPage,
             'endPage':endPage,
             'totPage':totPage,
             'currentPage': currentPage,
             'field':field,
             'word':word,
             'range' : range(startPage, endPage+1)}
  return render(request, 'board/list.html',context)      

# list_page
def list_page(request):
   page = request.GET.get('page', 1)
   word = request.GET.get('word','')

   boardCount = Board.objects.filter(
      Q(writer__contains = word)|
      Q(title__contains=word) |
      Q(content__contains=word)).count()
   
   boardList = Board.objects.filter(
      Q(writer__contains = word)|
      Q(title__contains=word) |
      Q(content__contains=word)).order_by('-id')
   
# 페이징 처리
   pageSize = 5

   paginator = Paginator(boardList,pageSize)
   page_obj = paginator.get_page(page)
   print('page_obj :' , page_obj)


   context = {
      'boardCount' : boardCount,
      'page_list' : page_obj,
      'word' : word
   }

   return render(request, 'board/list_page.html',context)


# detail
def detail(request, board_id):
   board = Board.objects.get(id=board_id)
   # 조회수 증가
   board.hit_up()
   board.save()
   
   return render(request, 'board/detail.html', {'board' :board})

# comment_insert
@csrf_exempt
def comment_insert(request):
   id = request.POST['id']
   comment = Comment(writer='aa', board_id=id,
                     content=request.POST['content'])
   comment.save()
   return redirect('/detail/'+id)