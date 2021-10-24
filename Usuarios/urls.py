from os import name
from django.contrib import admin
from django.urls import path
from .views import home, acceder, listarProductos, crearProductos, ingredientespage, modificarProductos
from Finanzas import views as fi
from django.conf.urls import include, url
#from django.contrib.auth.decorators import login_required


urlpatterns = [
  
   path('', acceder, name="inicio"),
   
]