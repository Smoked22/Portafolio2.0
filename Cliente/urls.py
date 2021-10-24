from os import name
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Cliente, name='homeCliente'),
]