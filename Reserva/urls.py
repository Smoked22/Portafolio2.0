from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('home/', home, name="homeReserva"),
    path('home/Listado_Reservas', reserva_listado, name="reserva_listado"),
    path('home/Crear_Reserva', reserva_crear, name="reserva_crear"),
    path('home/Mesas_Listado', mesas_listar, name="mesas_listar"),
    #path('home/reservas', reservas, name="reservas"),
    #path('home/crearReserva', crearReserva, name="crearReserva"),
    #path('home/crearCliente', crearCliente, name="crearCliente"),
    path('home/inicioReserva', inicioReserva, name="inicioReserva"),
    #path('home/modificarReserva', modificarReserva, name="modificarReserva"),
    #path('home/inicioReserva/listarClientes', listarClientes, name="listarClientes"),
    #path('home/inicioReserva/listadoModificar', listarClientesModificar, name="listarClientesModificar"),
    #path('home/inicioReserva/listadoModificar/modificarCliente/<id>/', modificarCliente, name="modificarCliente"),

]