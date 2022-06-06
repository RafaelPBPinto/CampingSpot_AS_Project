from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'polls/index.html')

def about(request):
    return render(request, 'polls/about.html')

def anpc(request):
    return render(request, 'polls/anpc.html')

def gallery(request):
    return render(request, 'polls/gallery.html')

def login(request):
    return render(request, 'polls/login.html')

