from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from myapp01.models import Board
from django.http.response import JsonResponse,HttpResponse
import urllib.parse



# Create your views here.


UPLOAD_DIR = 'C:/Django_Works/upload/'
# write_form
def write_form(request):
    return render(request, 'board/write.html')

# insert
@csrf_exempt
def insert(request):
        fname = ''
        fsize = 0
        if 'file' in request.FILES:
            file = request.FILES['file']
            fsize = file.size
            fname = file.name
            fp = open('%s%s' %(UPLOAD_DIR, fname), 'wb')
            for chunk in file.chunks():
                fp.write(chunk)
            fp.close()

# DTO 정의
        dto = Board(writer=request.POST['writer'],
                    title=request.POST['title'],
                    content=request.POST['content'],
                    filename=fname,
                    filesize=fsize
                    )
        dto.save()
        

        return redirect("/list/")

# list 전체보기(기본)
def list(request):
     boardList = Board.objects.all()
     context = {'boardList' : boardList}
     return render(request, 'board/list.html', context)

# 상세보기 : detail_idx 출력
# 출력할때 /detail_idx?idx=1와 같은 형태로 출력
def detail_idx(request):
     id = request.GET['idx']
     # print('id:' , id)
     dto = Board.objects.get(idx=id) # 하나의 Object를 return 시킴
     dto.hit_up()
     dto.save()
     return render(request, 'board/detail.html' ,{'dto' : dto}) 
# 직접적으로 Dictionary 줘서 변수 지정

# 상세보기 : detail/{num}과 같은 REST API로 출력
# /detail/1와 같은 형태로 출력 => detail/<int:board_idx>
def detail(request, board_idx):
    #  print('board_idx :', board_idx)
     dto = Board.objects.get(idx=board_idx)
     dto.hit_up()
     dto.save()
     return render(request, 'board/detail1.html', {'dto' : dto})

# delete : 삭제
def delete(request, board_idx):
    Board.objects.get(idx=board_idx).delete()
    return redirect("/list/")

# download_count : 다운로드 횟수 증가
def download_count(request):
     id = request.GET['idx']
     print('id', id)
     dto = Board.objects.get(idx=id)
     dto.down_up() # 다운로드 수 증가
     dto.save()
     count = dto.down # 다운로드 수
     print('count', count)
     return JsonResponse({'idx' : id, 'count' : count})

# download
def download(request):
    id = request.GET['idx']
    dto = Board.objects.get(idx=id)
    path = UPLOAD_DIR + dto.filename
    # filename = urllib.parse.quote(dto.filename)
    filename = dto.filename

    with open(path , 'rb') as file :
        response = HttpResponse(file.read(), 
                                 content_type = 'application/octet-stream')
        response['Content-Disposition'] = "attachment; filename*=UTF-8'{0}".format(filename) # filename 지정 없이 dto.filename을 써도 됨.
        return response
    
# update_form
def update_form(request, board_idx):
     dto = Board.objects.get(idx=board_idx)
     return render(request, 'board/update.html', {'dto' : dto})

# update
@csrf_exempt
def update(request):
    id = request.POST['idx']
    dto = Board.objects.get(idx=id)
    fname = dto.filename
    fsize = dto.filesize

## file 수정
    if 'file' in request.FILES:
            file = request.FILES['file']
            fsize = file.size
            fname = file.name
            fp = open('%s%s' %(UPLOAD_DIR, fname), 'wb')
            for chunk in file.chunks():
                fp.write(chunk)
            fp.close()

    dto_update = Board(id,
                    writer=request.POST['writer'],
                    title=request.POST['title'],
                    content=request.POST['content'],
                    filename=fname,
                    filesize=fsize)
    dto_update.save()


    return redirect("/list/")

# Comment
@csrf_exempt
def comment_insert(request):
    id = request.POST['idx']
    cdto = Comment(board_idx = id,
                   writer = 'aa',
                   content = request.POST['content'])
    cdto.save()
    return redirect("detail/"+id)
    # return redirect("detail_idx?idx="+id)