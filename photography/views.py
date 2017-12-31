from django.shortcuts import render
from django.http import HttpResponse
from .models import photography
# Create your views here.
def index(request):
    photos = photography.objects.all()
    return render(request, 'base.html', {'photos': photos})
def detail(request, photo_id):
    photo = photography.objects.get(id=photo_id)
    return render(request, 'detail.html', {'photo': photo})
def add(request):
    if(request.method == 'POSTS'):
        return
    else:
        return render(request, 'add.html')
