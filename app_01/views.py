from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from app_01.models import Post


def index(request):
    # return HttpResponse('hello world')
    now = datetime.now()
    posts = Post.objects.all()

    # for  process_exception
    # raise RuntimeError

    return render(request, 'index.html', {'posts': posts})
# Create your views here.
