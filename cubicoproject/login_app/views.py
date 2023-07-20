from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

class CustomLoginView(LoginView):
    template_name = 'login_app/login.html'
    
    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect('custom_dashboard')
    
    def form_invalid(self, form):
        error_message = 'Invalid username or password.'
        return render(self.request, self.template_name, {'error_message': error_message})


   #Una vez se inicie sesión 
def custom_dashboard_view(request):
    # Aquí puedes agregar la lógica para cargar los datos del panel personalizado
    # y renderizar la plantilla correspondiente
     return render(request, 'login_app/custom_dashboard.html')