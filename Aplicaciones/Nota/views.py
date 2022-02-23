from django.shortcuts import redirect, render
from .models import Nota
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    notas = Nota.objects.filter(propietario = request.user.username)
    return render(request, "gestionNotas.html", {"notas": notas})

#Create
@login_required
def creacionNota(request):
    return render(request, 'creacionNota.html')

@login_required
def crearNota(request):
    titulo = request.POST['txtTitulo']
    contenido = request.POST['txtContenido']
    ##propietario = request.POST['txtPropietario']

    usuario = Nota.objects.create(
        titulo = titulo,
        contenido = contenido,
        propietario = request.user.username
    )

    return redirect('/')

@login_required
def edicionNota(request, idNota):
    nota = Nota.objects.get(idNota = idNota)
    return render(request, 'edicionNota.html', {"nota":nota})

@login_required
def editarNota(request, idNota):
    titulo = request.POST['txtTitulo']
    contenido = request.POST['txtContenido']
  

    nota = Nota.objects.get(idNota=idNota)
    nota.titulo = titulo
    nota.contenido = contenido
    nota.save()

    return redirect('/')

@login_required
def eliminarNota(request, idNota):
    nota = Nota.objects.get(idNota = idNota)
    nota.delete()

    return redirect('/')


