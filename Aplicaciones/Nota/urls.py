from django.urls import path
from django.views import View
from . import views

urlpatterns = [
    path('', views.home),

    path('creacionNota/', views.creacionNota),
    path('crearNota/', views.crearNota),

    path('edicionNota/<idNota>', views.edicionNota),
    path('editarNota/<idNota>', views.editarNota),

    path('eliminarNota/<idNota>', views.eliminarNota)
]