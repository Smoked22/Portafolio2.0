from os import name
from django.contrib import admin
from django.urls import path, include
from .views import *
#from .views import home, acceder
from django.conf.urls import url
#from django.contrib.auth.decorators import login_required


urlpatterns = [
   path('home/', home, name="home_cocina"),
   path('home/receta/', receta, name="registro_receta"),
   path('home/Crear_Receta/', receta_crear, name="receta_crear"),
   path('home/Listar_Receta/', receta_listado, name="receta_listado"),

   path('home/Listar_Orden/', orden_listado, name="orden_listado"),
   path('home/Detalle_Orden/<id>/', orden_detalle, name="orden_detalle"),
   path('home/Actualizar_Orden/<id>/<sec>/<sec2>/', orden_actualizar, name="orden_actualizar"),

   #path('home/listar_ordenes/', ordenes, name="listar_ordenes"),
   #path('home/listar_recetas/', listar_recetas, name="listar_recetas"),
   #path('home/lista_recetamod/', modificar_receta, name="listar_recetamod"),
   #path('home/modificar_ordenes/', modificar_ordenes, name="modificar_ordenes"),
   #path('home/Buscar_receta/<id>', buscar_receta_lista, name="buscar_receta_lista"),
   path("select2/", include("django_select2.urls")),
   #path('', acceder, name="inicio"),
  
]