from django.shortcuts import render
from django.contrib.auth import authenticate, login
 
# Create your views here.
def login(request): #  vista

 if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('custom_dashboard')  # Redirige a la página de inicio personalizada
        else:
            # El usuario no está autenticado, muestra un mensaje de error
            error_message = 'Nombre de usuario o contraseña incorrectos.'
            return render(request, 'login_app/login.html', {'error_message': error_message})
 else:
        return render(request, 'login_app/login.html')