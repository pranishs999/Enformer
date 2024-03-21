from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login

def index(request):
    return render(request, 'index.html')


def logoutUser(request):
    logout(request)
    return redirect("/login")
