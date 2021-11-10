from os import name
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Cliente, name='homeCliente'),
    path('EnMesa/', ClienteEnMesa, name="clienteEnMesa"),
    path('ReservarMesa/', ReservarMesa, name="reservarMesa"),
    path('CancelarReserva/', CancelarReserva, name="cancelarReserva"),
    path('VerMenu/', VerMenu, name="verMenu"),
]