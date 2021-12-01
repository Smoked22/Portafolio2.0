from django.urls import path, include
from django.contrib import admin
from .views import *

urlpatterns = [
    path('home/', home_totem, name="totem_login"),
    path('home/login', totem_login, name="home_totem"),
    path('home/mensaje', totem_mensaje, name="totem_mensaje"),
    path('home/reservar/<id>/<sec>/', reservar_totem, name="reservar_totem")

]