from django.urls import path
from django.contrib import admin
from .views import home, reservas, crearReserva, crearCliente

urlpatterns = [
    path('home/', home, name="homeReserva"),
    path('home/reservas', reservas, name="reservas"),
    path('home/crearReserva', crearReserva, name="crearReserva"),
    path('home/crearCliente', crearCliente, name="crearCliente")
]