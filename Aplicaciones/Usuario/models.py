from pyexpat import model
from django.db import models

# Create your models here.

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    contrasena = models.CharField(max_length=20)

    def __str__(self) -> str:
        texto = "{0}-{1}"
        return texto.format(self.idUsuario, self.nombre)