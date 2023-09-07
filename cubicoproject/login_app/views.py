from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Proyecto, Tarea
from .forms import ProyectoForm  # formulario


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

    if request.method == 'POST':
        # Manejar la carga de archivos de planos y contratos
        if 'planos' in request.FILES:
            proyecto.planos = request.FILES['planos']
        
        if 'contratos' in request.FILES:
            proyecto.contratos = request.FILES['contratos']

        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        fecha_vencimiento = request.POST.get('fecha_vencimiento')

        # Comprobar si se proporcionó un título antes de crear la tarea
        if titulo:
            tarea_nueva = Tarea(
                proyecto=proyecto,
                titulo=titulo,
                descripcion=descripcion,
                fecha_vencimiento=fecha_vencimiento,
                completada=False  # Nueva tarea creada como pendiente
            )
            tarea_nueva.save()

        # Ahora, guarda los cambios en el modelo Proyecto
        proyecto.save()

        return redirect('detalle_proyecto', proyecto_id=proyecto_id)

    return render(request, 'login_app/detalle_proyecto.html', {'proyecto': proyecto, 'tareas_pendientes': tareas_pendientes, 'tareas_completadas': tareas_completadas})
 

def editar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('detalle_proyecto', proyecto_id=proyecto.id)
    else:
        form = ProyectoForm(instance=proyecto)
    
    return render(request, 'login_app/editar_proyecto.html', {'form': form, 'proyecto': proyecto})


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