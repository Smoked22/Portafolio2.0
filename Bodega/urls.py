from os import name
from django.contrib import admin
from django.urls import path
from .views import home
from .views import *
from django.conf.urls import url
#from django.contrib.auth.decorators import login_required


urlpatterns = [
   path('home/', home, name="home_bodega"),
   path('ingredientes/', ingredientes, name="registro_ingrediente"),
   #path('', acceder, name="inicio"),
  
]