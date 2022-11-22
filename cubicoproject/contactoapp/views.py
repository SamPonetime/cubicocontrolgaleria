from django.shortcuts import render

# Create your views here.

def contacto(request): #tercera vista

    return render(request,"contactoapp/contacto.html")

