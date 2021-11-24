from os import name
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls import url
#from django.contrib.auth.decorators import login_required


urlpatterns = [
   path('home/', home_finanzas, name="homefinanzas"),
   path('boletas/', boletas, name="boletas_finanzas"),
   path('proveedores/', proveedores, name="proveedores_finanzas"),
   path('proveedores/productos/<id>', listado_produc_proveedor, name="productos_proveedores"),
   path('guias_despacho/', guia_despacho, name="guias_desp_finanzas"),
   path('agregar_boleta/', agegar_boleta, name="agregar_boleta_finanzas"),
   path('grafico/', grafico, name="graficos_finanzas"),
   path('prueba/', prueba, name="prueba"),
]