from django.urls import path, include
from django.contrib import admin
from .views import *

urlpatterns = [
    path('home/', home, name="homeReserva"),
    path('pruebas/', pruebas, name="pruebas"),
    path('home/Listado_Reservas/', reserva_listado, name="reserva_listado"),
    path('home/Crear_Reserva/', reserva_crear, name="reserva_crear"),
    path('home/Mesas_Listado/', mesas_listar, name="mesas_listar"),
    path('home/Modificar_Reserva/<id>', reserva_modificar, name="reserva_modificar"),
    path('home/Eliminar_Reserva/<id>', reserva_eliminar, name="reserva_eliminar"),
    path('home/Listar_Horario_Mesa/<id>', horario_mesa, name="horario_mesa"),
    path('home/Buscar_Reserva/', reserva_buscar, name="reserva_buscar"),
    path("select2/", include("django_select2.urls")),
    #path('home/reservas', reservas, name="reservas"),
    #path('home/crearReserva', crearReserva, name="crearReserva"),
    #path('home/crearCliente', crearCliente, name="crearCliente"),
    path('home/inicioReserva', inicioReserva, name="inicioReserva"),
    #path('home/modificarReserva', modificarReserva, name="modificarReserva"),
    #path('home/inicioReserva/listarClientes', listarClientes, name="listarClientes"),
    #path('home/inicioReserva/listadoModificar', listarClientesModificar, name="listarClientesModificar"),
    #path('home/inicioReserva/listadoModificar/modificarCliente/<id>/', modificarCliente, name="modificarCliente"),

]