from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Proyecto
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
    context = {'username': username}
    return render(request, 'login_app/custom_dashboard.html', context)

def custom_dashboard_view(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'login_app/custom_dashboard.html', {'proyectos': proyectos})


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
  return render(request, 'login_app/detalle_proyecto.html', {'proyecto': proyecto})

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