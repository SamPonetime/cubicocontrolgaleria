import os
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Archivo, Proyecto, Tarea
from .forms import ProyectoForm  # formulario
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings


class CustomLoginView(LoginView):
    template_name = 'login_app/login.html'
    
    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect('custom_dashboard')
    
    def form_invalid(self, form):
        error_message = 'Invalid username or password.'
        return render(self.request, self.template_name, {'error_message': error_message})


@login_required # asegura que el usuario esté autenticado antes de acceder a la vista
def custom_dashboard_view(request):
    username = request.user.username
    proyectos = Proyecto.objects.all()
    query = request.GET.get('search_proyect')  # Obtener la consulta de búsqueda del parámetro GET 'q'
    
    if query:
        # Filtrar proyectos que coincidan con la consulta - icontains=operador de consulta mayus o minusculas
        proyectos = proyectos.filter(nombre__icontains=query)
    
    context = {'username': username, 'proyectos': proyectos}
    return render(request, 'login_app/custom_dashboard.html', context)


def agregar_proyecto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        ubicacion = request.POST['ubicacion']
        cliente = request.POST['cliente']
        presupuesto = request.POST['presupuesto']
        fecha_inicio = request.POST['fecha_inicio']
        fecha_fin = request.POST['fecha_fin']
        
        proyecto = Proyecto(nombre=nombre, ubicacion=ubicacion, cliente=cliente,
                            presupuesto=presupuesto, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)
        proyecto.save()
        return redirect('custom_dashboard')
    else:
        return render(request, 'login_app/agregar_proyecto.html')
    

def detalle_proyecto(request, proyecto_id):

    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    tareas_pendientes = Tarea.objects.filter(proyecto=proyecto, completada=False)
    tareas_completadas = Tarea.objects.filter(proyecto=proyecto, completada=True)
    # Consulta actualizada de archivos para el proyecto
    archivos_proyecto = proyecto.planos.all() | proyecto.contratos.all()

    if request.method == 'POST':
        # Comprobar si se proporcionó un título antes de crear la tarea
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        fecha_vencimiento = request.POST.get('fecha_vencimiento')

        if titulo:
            tarea_nueva = Tarea(
                proyecto=proyecto,
                titulo=titulo,
                descripcion=descripcion,
                fecha_vencimiento=fecha_vencimiento,
                completada=False
            )
            tarea_nueva.save()

        proyecto.save()

        # Manejar la carga de archivos de planos y contratos después de guardar el proyecto
        for archivo_plano in request.FILES.getlist('planos'):
            nuevo_plano = Archivo(archivo=archivo_plano)
            nuevo_plano.proyecto = proyecto  # Asignar el proyecto a la instancia del archivo
            nuevo_plano.save()
            proyecto.planos.add(nuevo_plano)
    
        for archivo_contrato in request.FILES.getlist('contratos'):
            nuevo_contrato = Archivo(archivo=archivo_contrato)
            nuevo_contrato.proyecto = proyecto  # Asignar el proyecto a la instancia del archivo
            nuevo_contrato.save()
            proyecto.contratos.add(nuevo_contrato)
       
        return redirect('detalle_proyecto', proyecto_id=proyecto.id)

    return render(request, 'login_app/detalle_proyecto.html', {'proyecto': proyecto, 'tareas_pendientes': tareas_pendientes, 'tareas_completadas': tareas_completadas})

def editar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    tareas_pendientes = Tarea.objects.filter(proyecto=proyecto, completada=False)
    tareas_completadas = Tarea.objects.filter(proyecto=proyecto, completada=True)

    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)

        if form.is_valid():
            form.save()
            return redirect('detalle_proyecto', proyecto_id=proyecto.id)
    else:
        form = ProyectoForm(instance=proyecto)

    return render(request, 'login_app/editar_proyecto.html', {'form': form, 'proyecto': proyecto, 'tareas_pendientes': tareas_pendientes, 'tareas_completadas': tareas_completadas})

def eliminar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    if request.method == 'POST':
        proyecto.delete()
        return redirect('custom_dashboard')
    return render(request, 'login_app/eliminar_proyecto.html', {'proyecto': proyecto})

def marcar_tarea_completada(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.completada = not tarea.completada
    tarea.save()
    return redirect('detalle_proyecto', proyecto_id=tarea.proyecto.id)

def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.delete()
    return redirect('editar_proyecto', proyecto_id=tarea.proyecto.id)

def eliminar_archivo(request, archivo_id):
    archivo = get_object_or_404(Archivo, id=archivo_id)
    
    # Eliminar físicamente el archivo del sistema de archivos
    ruta_archivo = os.path.join(settings.MEDIA_ROOT, str(archivo.archivo))
    if os.path.exists(ruta_archivo):
        os.remove(ruta_archivo)

    # Eliminar la entrada del archivo de la base de datos
    archivo.delete()
    
    # Redirigir de nuevo a la vista de detalles
    return HttpResponseRedirect(reverse('detalle_proyecto', args=[archivo.proyecto.id]))