from os import name
from django.contrib import admin
from django.urls import path
from .views import home, acceder
from Finanzas import views as fi
from django.conf.urls import url
#from django.contrib.auth.decorators import login_required


urlpatterns = [
   path('home/', home, name="home"),
   path('', acceder, name="inicio"),
   path('home/finanzas/',fi.home_finanzas, name="homefinanzas"),
]