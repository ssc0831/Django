from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from myapp02.models import Board
from .form import UserForm

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