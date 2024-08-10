from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView

class IndexView(TemplateView):
    template_name ='index.html'


def index(request):
    return render(request, 'signup.html')


def logoutUser(request):
    logout(request)
    return redirect("/login")
