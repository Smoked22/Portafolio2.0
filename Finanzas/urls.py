from os import name
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls import url
#from django.contrib.auth.decorators import login_required


urlpatterns = [
   path('home/', home_finanzas, name="homefinanzas"),
   path('boletas/', boletas, name="boletas_finanzas"),
]