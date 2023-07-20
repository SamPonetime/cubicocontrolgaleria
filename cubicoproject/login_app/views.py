from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

class CustomLoginView(LoginView):
    template_name = 'login_app/login.html'
    
    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect('custom_dashboard')
    
    def form_invalid(self, form):
        error_message = 'Invalid username or password.'
        return render(self.request, self.template_name, {'error_message': error_message})


@login_required
def custom_dashboard_view(request):
    username = request.user.username
    context = {'username': username}
    return render(request, 'login_app/custom_dashboard.html', context)