"""cubicoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import CustomLoginView

from login_app import views 

 
urlpatterns = [
    
 
    path('login/', CustomLoginView.as_view(), name='Login'),
 
    path('custom_dashboard/', views.custom_dashboard_view, name='custom_dashboard'),  
 
    path('agregar_proyecto/', views.agregar_proyecto, name='agregar_proyecto'),  
  
    path('detalle_proyecto/<int:proyecto_id>/', views.detalle_proyecto, name='detalle_proyecto'),

    path('editar_proyecto/<int:proyecto_id>/', views.editar_proyecto, name='editar_proyecto'),
    
    path('eliminar_proyecto/<int:proyecto_id>/', views.eliminar_proyecto, name='eliminar_proyecto'),

    path('marcar_completada/<int:tarea_id>/', views.marcar_tarea_completada, name='marcar_completada'),

]
 