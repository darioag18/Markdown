from django.db import models

# Create your models here.

class Nota(models.Model):
    idNota = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=75)
    contenido = models.CharField(max_length=2000)
    propietario = models.CharField(max_length=20)


    def __str__(self) -> str:
        texto = "{0}-{1}"
        return texto.format(self.idNota, self.titulo)