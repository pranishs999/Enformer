from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views import View

class IndexView(TemplateView):
    template_name ='index.html'
    
    
class LoginView(TemplateView):
    template_name = 'signin.html'

def logoutUser(request):
    logout(request)
    return redirect("/login")
