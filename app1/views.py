from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name ='index.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')  

