from django.urls import path
from django.contrib import admin
from .views import home, reservas

urlpatterns = [
    path('home/', home, name="homeReserva"),
    path('home/reservas', reservas, name="reservas")
]