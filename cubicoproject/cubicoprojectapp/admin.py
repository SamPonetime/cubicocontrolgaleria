from django.contrib import admin

from cubicoprojectapp.models import galeria_proyectos
 


class GaleriaAdmin(admin.ModelAdmin):
    list_display=("nombre","descripcion") #Lo que debe mostrar en el listado de la tabla
    search_fields=("nombre","descripcion") #Puede filtrar busquedas en relación a..
  #  list_filter=("fechasubida",)

# Modelos aquí.
admin.site.register(galeria_proyectos, GaleriaAdmin) #brinda acceso al modelo desde el panel y usa la clase creada GaleriaAdmin

