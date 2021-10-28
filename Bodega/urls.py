from os import name
from django.contrib import admin
from django.urls import path
from .views import home
from django.conf.urls import url
#from django.contrib.auth.decorators import login_required


urlpatterns = [
   path('home/', home, name="home_bodega"),
   #path('', acceder, name="inicio"),
  
]