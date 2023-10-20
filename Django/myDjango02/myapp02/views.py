from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from myapp02.models import Board
from .form import UserForm
from django.db.models import Q

import urllib.parse
import math

# Create your views here.

# signup
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            print("Aa")
            form.save()
        else:
            print("bbb")
    else:
        form = UserForm()

    return render(request, 'common/signup.html', {'form' : form})


UPLOAD_DIR ='C:/Django_Works/upload/'
# write_form
def write_form(request):
    return render(request, 'board/insert.html')

# insert
@csrf_exempt
def insert(request):
    fname = ''
    fsize =0
    if 'file' in request.FILES :
        file = request.FILES['file']
        fsize = file.size
        fname = file.name
        fp = open('%s%s' %(UPLOAD_DIR, fname), 'wb')
        for  chunk  in file.chunks():
            fp.write(chunk)
        fp.close()    

    board = Board(writer=request.POST['writer'],
                title =request.POST['title'],
                content = request.POST['content'],
                filename = fname,
                filesize = fsize               
                )    
    board.save()
    return redirect("/list/")


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