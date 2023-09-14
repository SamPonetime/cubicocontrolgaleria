from django import forms
from .models import Proyecto, Tarea, Archivo

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'
 

class ArchivoForm(forms.ModelForm):
    proyecto = forms.ModelChoiceField(queryset=Proyecto.objects.all(), widget=forms.HiddenInput())
    eliminar_archivos = forms.ModelMultipleChoiceField(queryset=Archivo.objects.none(), required=False, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Archivo
        fields = ['archivo', 'proyecto']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        proyecto = self.instance  # Obtener la instancia de Proyecto asociada
        self.fields['eliminar_archivos'].queryset = proyecto.planos.all() | proyecto.contratos.all()



class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_vencimiento']
