from django import forms
from .models import Proyecto, Tarea, Archivo

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'  # Esto incluirá todos los campos del modelo en el formulario

class ArchivoForm(forms.ModelForm):
    proyecto = forms.ModelChoiceField(queryset=Proyecto.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Archivo
        fields = ['archivo', 'proyecto']  # Agrega el campo proyecto al formulario

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_vencimiento']