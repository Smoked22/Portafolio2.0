from os import name
from django.contrib import admin
from django.urls import path
from .views import *
from Finanzas import views as fi
from django.conf.urls import include, url
#from django.contrib.auth.decorators import login_required


urlpatterns = [
   path('home/', home, name="home"),
   path('home/ingrediente/listarIngrediente', listarProductos, name="listarProductos"),
   path('home/ingrediente/crearIngrediente/', crearProductos, name="crearProductos"),
   path('home/ingrediente/modificarIngrediente/<id>', modificarProductos, name="modificarProductos"),
   path('home/ingrediente/', ingredientespage, name="ingredientespage"),
]