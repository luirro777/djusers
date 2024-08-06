from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import CustomUser 

class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class UserLoginView(LoginView):
    template_name = 'login.html'

class UserProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser  
    template_name = 'profile.html'
    context_object_name = 'user'
    
    def get_object(self, queryset=None):
        return self.request.user

