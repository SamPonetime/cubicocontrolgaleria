from django.shortcuts import render



# Create your views here.
def index(request): #primera vista

    return render(request,"index.html")


def nosotros(request): #segunda vista

    return render(request,"nosotros.html")

    

def contacto(request): #tercera vista

    return render(request,"contacto.html")


def projects(request):
    return render(request,"projects.html") #faltaría un tercer argumento con el contexto(diccionario)
 