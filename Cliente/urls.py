from os import name
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Cliente, name='homeCliente'),
    path('EnMesa/', ClienteEnMesa, name="clienteEnMesa"),
    path('Reservar/', Reservar, name="reservar"),
    path('ReservarMesa/', ReservarMesa, name="reservarMesa"),
    path('CancelarReserva/', CancelarReserva, name="cancelarReserva"),
    path('VerMenu/', VerMenu, name="verMenu"),
    path('CrearCliente/', ClienteCrear, name="clienteCrear"),
    path('Menu_Entrada/', MenuEntrada, name="menuEntrada"),
    path('Menu_Fondo/', MenuFondo, name="menuFondo"),
    path('Menu_Postre/', MenuPostre, name="menuPostre"),
    path('Menu_Beber/', MenuBeber, name="menuBebidas"),
]