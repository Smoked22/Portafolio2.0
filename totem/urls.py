from django.urls import path, include
from django.contrib import admin
from .views import *

urlpatterns = [
    path('home/', home_totem, name="home_totem"),
    path('home/reservar/<id>/<sec>/', reservar_totem, name="reservar_totem")

]