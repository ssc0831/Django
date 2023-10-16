from django.shortcuts import render, redirect
from django.http.response import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from myapp01.models import Board, Comment

import urllib.parse

# Create your views here.


UPLOAD_DIR ='D:/____BIG13_JUNG/__LECTURE/DjangoWork/upload/'
# write_from
def write_form(request):
    return render(request,'board/write.html')

# insert
@csrf_exempt
def insert(request):
    fname = ''
    fsize =0
    if 'file' in request.FILES :
        file = request.FILES['file']
        fsize = file.size
        fname = file.name
        fp =open('%s%s' %(UPLOAD_DIR,fname ), 'wb')
        for  chunk  in file.chunks():
            fp.write(chunk)
        fp.close()    

    dto = Board(writer=request.POST['writer'],
                title =request.POST['title'],
                content = request.POST['content'],
                filename = fname,
                filesize = fsize               
                )    
    dto.save()

    return redirect("/list/")

# list 전체보기(기본)
def list(request):
    boardList =  Board.objects.all()
    boardCount = Board.objects.all().count()
    context = {'boardList' : boardList}
    return render(request, 'board/list.html',context)

# detail_idx : 상세보기  /detail_idx?idx=1
def detail_idx(request):
    id = request.GET['idx']
    # print('id :' , id)
    dto = Board.objects.get(idx=id)
    dto.hit_up()
    dto.save()
    return render(request, 'board/detail.html',
                  {'dto': dto})


# detail : 상세보기  /detail/1 ==>  detail/<int:board_idx>
def detail(request, board_idx):
#     print('board_idx : ' , board_idx)
    dto = Board.objects.get(idx=board_idx)
    dto.hit_up()
    dto.save()
    ###### comment list
    commentList =Comment.objects.filter(board_idx =board_idx).order_by('-idx') 
    commentCnt = Comment.objects.filter(board_idx=board_idx).count
    print('commentList sql : ',commentList.query )
   
    return render(request, 'board/detail.html',
                  {'dto': dto , 'commentList' : commentList,'commentCnt' : commentCnt })

# delete : 삭제
def delete(request,board_idx) : 
    Board.objects.get(idx=board_idx).delete()
    return redirect("/list/")   

# update_form
def update_form(request,board_idx):
    dto = Board.objects.get(idx=board_idx)
    return render(request, 'board/update.html',{'dto': dto})

# update
@csrf_exempt
def update(request):
    id = request.POST['idx']
    dto = Board.objects.get(idx = id)
    fname = dto.filename
    fsize = dto.filesize
    ###  file 수정
    if 'file' in request.FILES :
        file = request.FILES['file']
        fsize = file.size
        fname = file.name
        fp =open('%s%s' %(UPLOAD_DIR,fname ), 'wb')
        for  chunk  in file.chunks():
            fp.write(chunk)
        fp.close()    

    dto_update  = Board(id,
                writer=request.POST['writer'],
                title =request.POST['title'],
                content = request.POST['content'],
                filename = fname,
                filesize = fsize)
    dto_update.save()

    return redirect("/list/")   



#  download_count
def download_count(request):
    id = request.GET['idx']
    print('id : ', id)  
    dto = Board.objects.get(idx = id)
    dto.down_up() # 다운로드 수 증가
    dto.save()
    count = dto.down  # 다운로드 수
    print('count : ', count)
    return JsonResponse ({'idx' : id , 'count': count })   

#   download   
def download(request):
    id= request.GET['idx']
    dto = Board.objects.get(idx = id)
    path = UPLOAD_DIR + dto.filename
    filename = urllib.parse.quote(dto.filename)
    # filename = dto.filename

    with open(path ,'rb') as file :
        response = HttpResponse(file.read(),
                               content_type='application/octet-stream')
        response['Content-Disposition']="attachment;filename*=UTF-8''{0}".format(filename)    

    return response

### comment
@csrf_exempt
def comment_insert(request):
    id = request.POST['idx']
    cdto = Comment(board_idx = id,
               writer = 'aa',
               content = request.POST['content'])
    cdto.save()

    # return redirect("/detail_idx?idx="+id)
    return redirect("/detail/"+id)
