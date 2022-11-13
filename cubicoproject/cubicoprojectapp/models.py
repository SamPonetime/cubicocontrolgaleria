from django.db import models

# Create your models here.

class galeria_proyectos(models.Model):
    imagen=models.ImageField(verbose_name="Imagen del proyecto")
    nombre=models.CharField(max_length=100,verbose_name="Nombre del proyecto")
    descripcion=models.CharField(max_length=500,verbose_name="descripción general")
   

    def __str__(self):
        return self.nombre #Método Devuelve el "nombre" del proyecto para utilizarlo cmo titulo (listado y vista individual)