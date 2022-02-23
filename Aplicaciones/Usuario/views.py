
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

from Aplicaciones.Usuario.forms import UserRegisterForm

def registrar(request):
    if request.method == 'POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            
            return redirect('/login')
    else:
        form = UserCreationForm()
    context = {'form' : form}
    return render(request, 'registrar.html', context)