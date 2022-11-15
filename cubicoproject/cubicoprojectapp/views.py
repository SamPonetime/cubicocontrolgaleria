from django.shortcuts import render
from cubicoprojectapp.models import galeria_proyectos


# Create your views here.
def index(request): #primera vista

    return render(request,"cubicoprojectapp/index.html")


def nosotros(request): #segunda vista

    return render(request,"cubicoprojectapp/nosotros.html")

    

def contacto(request): #tercera vista

    return render(request,"cubicoprojectapp/contacto.html")


def projects(request):
    proyectos=galeria_proyectos.objects.all() #imporatar todos los registros de galeria_proyectos
    return render(request,"cubicoprojectapp/projects.html", {"proyectos":proyectos}) #faltaría un tercer argumento con el contexto(diccionario)
 