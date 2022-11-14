from django.shortcuts import render



# Create your views here.
def index(request): #primera vista

    return render(request,"cubicoprojectapp/index.html")


def nosotros(request): #segunda vista

    return render(request,"cubicoprojectapp/nosotros.html")

    

def contacto(request): #tercera vista

    return render(request,"cubicoprojectapp/contacto.html")


def projects(request):
    return render(request,"cubicoprojectapp/projects.html") #faltaría un tercer argumento con el contexto(diccionario)
 