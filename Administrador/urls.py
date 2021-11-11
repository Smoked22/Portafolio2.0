from os import name
from django.contrib import admin
from django.urls import path
from .views import *
from Finanzas import views as fi
from django.conf.urls import include, url
#from django.contrib.auth.decorators import login_required


urlpatterns = [
   path('home/', home_admin, name="home_admin"),
   path('home/empleados', empleados, name="empleados"),
   path('home/detalle_empleado/<id>', detalle_empleado, name="detalle_empleado"),
   path('home/ingrediente/listarIngrediente', listarProductos, name="listarProductos"),
   path('home/ingrediente/crearIngrediente/', crearProductos, name="crearProductos"),
   path('home/ingrediente/modificarIngrediente/<id>', modificarProductos, name="modificarProductos"),
   path('home/ingrediente/', ingredientespage, name="ingredientespage"),
   path('reservas/informe_reservas', informe_reservas, name="informe_reservas"),
   path('reservas/listar_reservas', listar_reservas_admin, name="listar_reservas_admin"),
   path('reservas/crear_reservas', crear_reservas_admin, name="crear_reservas_admin"),
]