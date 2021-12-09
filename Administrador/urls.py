from os import name
from django.contrib import admin
from django.urls import path
from .views import *
from Finanzas import views as fi
from django.conf.urls import include, url
#from django.contrib.auth.decorators import login_required


urlpatterns = [
   path('home/', home_admin, name="home_admin"),

   #EMPLEADOS
   path('home/empleados', empleados, name="empleados"),
   path('home/detalle_empleado/<id>', detalle_empleado, name="detalle_empleado"),

   #RESERVA
   path('home/informe_reservas', informe_reservas, name="informe_reservas"),
   path('home/listar_reservas', listar_reservas_admin, name="listar_reservas_admin"),
   path('home/crear_reservas', crear_reservas_admin, name="crear_reservas_admin"),
   path('home/listado_reserva_detalle', listar_reservas_detalle_admin, name="listar_reservas_detalle_admin"),

   #CLIENTE
   path('home/Crear_Cliente/', cliente_crear, name="cliente_crear_admin"),
   path('home/Listado_Cliente/', cliente_listado, name="cliente_listado_admin"),
   path('home/Cliente_modificar/<id>', cliente_modificar, name="cliente_modificar_admin"),
   path('home/Cliente_Eliminar/<id>', cliente_eliminar, name="cliente_eliminar_admin"),

   #Finanzas
   path('registro_boletas/', registro_boletas, name="registro_boleta_admin"),
   path('ingresar_boleta/', ingresar_boleta_admin, name="ingresar_boleta_admin"),
   path('proveedores/', lista_proveedor_admin, name="lista_proveedor_admin"),
   path('productos_proveedores/<id>', productos_proveedor_admin, name="productos_proveedor_admin"),
   path('graficos', graficos_admin, name="graficos_admin"),
   
]