from django.db import models
import os
from datetime import datetime
import logging


# Create your models here.

def archivo_ruta(instance, filename):
    # Obtener la extensión del archivo original
    file_extension = filename.split('.')[-1]

    # Obtener el id del proyecto desde la instancia del archivo
    proyecto_id = instance.proyecto.id
    
    # Generar un nombre de archivo único basado en el fecha y hora actual
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archivo_nombre = f"{timestamp}.{file_extension}"
    
    # Crear una ruta única basada en el nombre de archivo generado y el id del proyecto
    ruta = f'proyectos/{proyecto_id}/{archivo_nombre}'
    
    return ruta


class Archivo(models.Model):
    archivo = models.FileField(upload_to=archivo_ruta)
    

    def __str__(self):
        return self.archivo.name
    
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    cliente = models.CharField(max_length=100)
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
 # Campos para planos y contratos
    planos = models.ManyToManyField('Archivo', related_name='proyectos_planos', blank=True) 
    contratos = models.ManyToManyField('Archivo', related_name='proyectos_contratos', blank=True) 
   
    def __str__(self):
        return self.nombre


#tareas dentro de cada proyecto
class Tarea(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE) #si se elimina un proyecto, todas las tareas relacionadas con ese proyecto también se eliminarán. 
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_vencimiento = models.DateField()
    completada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
    
 