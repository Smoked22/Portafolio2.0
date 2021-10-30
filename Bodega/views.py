from django.shortcuts import redirect, render, redirect, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
# Create your views here.

@login_required
def home(request):
    return render(request, './home_bodega.html')

@login_required
def ingredientes(request):
    data = {
        'ingredientes':listado_ingredienter()
         
    }
    
    return render(request, './registro_ingrediente.html', data)

def listado_ingredienter():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_INGREDIENTER", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista
# LISTADOCATEGORIA
def listar_categoria():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_CATEGORIASR", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista





def agregar_ingrediente(request):
    
    data = {
        'categorias' :listar_categoria()
    }
    return render(request, './agregar_ingrediente.html' , data)

