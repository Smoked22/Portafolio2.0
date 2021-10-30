from os import name
from django.contrib import admin
from django.urls import path
from .views import home
from .views import *
from django.conf.urls import url
#from django.contrib.auth.decorators import login_required


urlpatterns = [
   path('home/', home, name="home_bodega"),
   path('home/ingredientes/', ingredientes, name="registro_ingrediente"),
   path('home/agregar_ingrediente/', agregar_ingrediente, name="agregar_producto_listado"),
   
   #path('', acceder, name="inicio"),
  
]