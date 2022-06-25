from django.shortcuts import render
from django.http import HttpResponse
from .models import Parque, Reserva
from django.contrib.auth.decorators import login_required
from datetime import date

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
        parques = Parque.objects.filter(nome__icontains=searched)
        distrito = Parque.objects.filter(location__icontains=searched)
        return render(request, 'polls/search.html', {'searched':searched, 'parques': parques, 'distrito': distrito, 'all': Parque.objects.all()})
    else:
        return render(request, 'polls/search.html', {})

def reservation(request):
    if request.method == "POST":
        reserva = request.POST.get('reserva', False)
        parques = Parque.objects.filter(nome__contains=reserva)
        return render(request, 'polls/reservation.html', {'reserva': reserva, 'parques': parques})
    else:
        return render(request, 'polls/reservation.html')

@login_required
def payment(request):
    if request.method == "POST":
        datai = request.POST.get('datai')
        dataf = request.POST.get('dataf')
        atividade = request.POST.get('atividade')
        pessoa = request.POST.get('pessoa')
        parque = request.POST.get('parque')
        preco = request.POST.get('preco')
        npessoas = request.POST.get('npessoas')
        delta = date(int(dataf[0:4]), int(dataf[5:7]), int(dataf[8:])) - date(int(datai[0:4]), int(datai[5:7]), int(datai[-2:]))
        preco = float(preco) * float(npessoas) * float(delta.days)
        if atividade == None:
            Reserva.objects.create(datei=datai, datef=dataf, price=preco, client_id=pessoa, parque_id=parque, npessoas=npessoas, days=delta.days)
            Reserva.objects.order_by('datei')
        else:
            Reserva.objects.create(datei=datai, datef=dataf,activity=atividade, price=preco, client_id=pessoa, parque_id=parque, days=delta.days)
            Reserva.objects.order_by('datei')
        return render(request, 'polls/payment.html', {'preco' : preco})
    else:
        return render(request, 'polls/payment.html')

@login_required
def confirmation(request):
    return render(request, 'polls/confirmation.html')
