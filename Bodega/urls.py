from os import name
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls import url
from django.urls import path, include
#from django.contrib.auth.decorators import login_required


urlpatterns = [
   path('home/', home, name="home_bodega"),
   path('home/ingredientes/', ingredientes, name="registro_ingrediente"),
   path('home/agregar_ingrediente/', agregar_ingrediente, name="agregar_producto_listado"),
   path('home/listar_suministros/', suministro, name="listar_suministros"),
   path('home/listar_proveedores/', proveedor, name="listar_proovedores"),
   path('home/lista_ingredientemod/', modificar_ingrediente, name="listar_ingredientemod"),
   path('home/modificar_ingrediente/<id>', modificar_ingrediente_rellenar, name="modificar_ingrediente_rellenar"),
   # path('home/Buscar_ingrediente/<id>', buscar_ingrediente_lista, name="buscar_ingrediente_lista"),
   path('home/eliminar_ingrediente/<id>', ingrediente_eliminar , name="ingrediente_eliminar"),
   path("select2/", include("django_select2.urls")),
   #path('', acceder, name="inicio"),
  
]