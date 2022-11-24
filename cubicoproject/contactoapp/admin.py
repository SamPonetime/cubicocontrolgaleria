from django.contrib import admin
from contactoapp.models import cubico_dato
# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    list_display=("correo","telefono", "tipo") #Lo que debe mostrar en el listado de la tabla
    search_fields=("correo","telefono","tipo") #Puede filtrar busquedas en relación a..
    
# Modelos aquí.
admin.site.register(cubico_dato, ContactoAdmin) #brinda acceso al modelo desde el panel y usa la clase creada ContactoAdmin

