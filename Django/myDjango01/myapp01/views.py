from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from myapp01.models import Board
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