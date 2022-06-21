from audioop import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from polls.models import Reserva,Parque
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth.middleware import AuthenticationMiddleware
from django.utils import timezone
from django.http import HttpResponseRedirect

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'A tua conta foi criada com sucesso! Agora podes fazer login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def historico(request):
    cliente = request.user
    reservas = Reserva.objects.filter(client_id=cliente.id)
    now = timezone.now().date()
    return render(request, 'users/historico.html',{'cliente':cliente.id, 'reservas':reservas.order_by('-datei'), 'time':now})
    
def delete(request, id):
    reserva = Reserva.objects.filter(id=id)
    reserva.delete()
    return HttpResponseRedirect('/historico')

def avaliaçao(request):
    cliente = request.user
    reservas = Reserva.objects.filter(client_id=cliente.id)
    now = timezone.now().date()
    if request.method == 'POST':
        messages.success(request, f'Avaliaçao feita com sucesso')
        return render(request, 'users/profile.html',{'cliente':cliente.id, 'reservas':reservas.order_by('-datei'), 'time':now})
        
    return render(request, 'users/avaliaçao.html',{'cliente':cliente.id, 'reservas':reservas.order_by('-datei'), 'time':now})

def sugestao(request):
    return render(request, 'users/sugestao.html')

def confirmaçao(request):
    return render(request, 'users/confirmaçao.html')