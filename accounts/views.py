from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView
from .forms import UserRegistrationForm
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import logout
from .forms import UserUpdateForm

# Create your views here.

class UserRegistrationView(CreateView):
    template_name='accounts/registration.html'
    form_class=UserRegistrationForm
    success_url=reverse_lazy('login')
    
    def form_valid(self,form):
        response=super().form_valid(form)
        messages.success(self.request,'Account Created Successfully')
        return response
    
    
class UserLoginView(LoginView):
    template_name='accounts/login.html'
    def get_success_url(self):
        return reverse_lazy ('profile')


def UserLogoutView(request):
    logout(request)
    return redirect('login')

class Profile(UpdateView):
    model=User
    form_class=UserUpdateForm
    template_name='accounts/profile.html'
    success_url=reverse_lazy('profile')
    
    def get_object(self):
        return self.request.user
    