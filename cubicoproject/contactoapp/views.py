from django.shortcuts import render
from contactoapp.models import cubico_dato


# Create your views here.

def contacto(request): #tercera vista

    cubico_contacto=cubico_dato.objects.get(tipo="Activo") #importar registros con tipo = "activo" de cubico_dato (solo debería ser uno)
    return render(request,"contactoapp/contacto.html", {"cubicodato":cubico_contacto}) #solicitud, plantilla y contexto(diccionario)


 