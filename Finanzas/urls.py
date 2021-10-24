from os import name
from django.contrib import admin
from django.urls import path
from .views import home_finanzas
from django.conf.urls import url
#from django.contrib.auth.decorators import login_required


urlpatterns = [
   path('home/', home_finanzas, name="homefinanzas"),
]