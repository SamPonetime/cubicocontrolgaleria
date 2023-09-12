from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    cliente = models.CharField(max_length=100)
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
 # Campos para planos y contratos
    planos = models.FileField(upload_to='planos/', blank=True, null=True) 
    contratos = models.FileField(upload_to='contratos/', blank=True, null=True)



#tareas dentro de cada proyecto
class Tarea(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE) #si se elimina un proyecto, todas las tareas relacionadas con ese proyecto también se eliminarán. 
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_vencimiento = models.DateField()
    completada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo