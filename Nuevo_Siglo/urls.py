"""Nuevo_Siglo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django import template
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Usuarios.urls')),
    path('Bodega/', include('Bodega.urls')),
    path('Cocina/', include('Cocina.urls')),
    path('Finanzas/', include('Finanzas.urls')),
    path('Cliente/', include('Cliente.urls')),
    path('Reserva/', include('Reserva.urls')),
    path('totem/', include('totem.urls')),
    path('Administrador/', include('Administrador.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path("select2/", include("django_select2.urls")),
    
    #path para importar las vistas de PWA
    path('',include('pwa.urls')),
]

admin.site.site_header = 'Administrador de Restaurante'
admin.site.index_title = 'Modulo de administración'
admin.site.site_title = 'Siglo XXI'

#hola perro dani te paso por el pico
#Hola perro dani yo igual te paso por el pico
#hola perro dani yo tambien te paso por el pico x3