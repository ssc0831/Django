from django.shortcuts import render

# Create your views here.
# write_form
def write_form(request):
    return render(request, 'board/insert.html')