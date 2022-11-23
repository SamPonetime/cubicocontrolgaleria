from django.db import models

# Create your models here.
class cubico_dato(models.Model):
    tipo=models.CharField(max_length=100,verbose_name="Activo o inactivo")
    correo=models.EmailField(max_length=50,verbose_name="Correo electrónico")
    telefono=models.BigIntegerField(verbose_name="Teléfono")

    def __str__(self):
        return self.correo #Método Devuelve el "correo" del proyecto para utilizarlo como titulo (listado y vista individual)
