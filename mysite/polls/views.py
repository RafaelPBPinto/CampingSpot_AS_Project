from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'polls/exemplo_home.html')

def about(request):
    return HttpResponse('<h1>Hello About</h1>')