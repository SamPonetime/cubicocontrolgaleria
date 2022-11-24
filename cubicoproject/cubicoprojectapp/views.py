from django.shortcuts import render
from cubicoprojectapp.models import galeria_proyectos

 
# Create your views here.
def index(request): #primera vista

    return render(request,"cubicoprojectapp/index.html")


def nosotros(request): #segunda vista

    return render(request,"cubicoprojectapp/nosotros.html")

    

def projects(request):
    proyectos=galeria_proyectos.objects.all() #importar todos los registros de galeria_proyectos
    return render(request,"cubicoprojectapp/projects.html", {"proyecto":proyectos}) #solicitud, plantilla y contexto(diccionario)


 

 