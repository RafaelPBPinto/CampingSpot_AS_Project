from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from polls.models import Reserva
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

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
    if request == "POST":
        cliente = request.POST.get('id_user',False)
        reservas = Reserva.objects.filter(client_id__contains=cliente)
        return render(request, 'users/historico.html',{'cliente':cliente, 'reservas':reservas})
    else:
        return render(request, 'users/historico.html')
