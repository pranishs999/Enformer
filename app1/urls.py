from django import views
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app1.views import *

urlpatterns = [
   path('', IndexView.as_view()),
]