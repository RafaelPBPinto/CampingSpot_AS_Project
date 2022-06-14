from django.shortcuts import render
from django.http import HttpResponse
from .models import Parque, Reserva

def index(request):
    list = {
        'parques': Parque.objects.all()
    }
    return render(request, 'polls/index.html', list)

def about(request):
    return render(request, 'polls/about.html')

def gallery(request):
    list = {
        'parques': Parque.objects.all()
    }
    return render(request, 'polls/gallery.html', list)

def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched', False)
        parques = Parque.objects.filter(nome__contains=searched)
        distrito = Parque.objects.filter(location__contains=searched)
        return render(request, 'polls/search.html', {'searched':searched, 'parques': parques, 'distrito': distrito, 'all': Parque.objects.all()})
    else:
        return render(request, 'polls/search.html', {})
