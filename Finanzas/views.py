from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db import connection

# Create your views here.

@login_required
def home_finanzas(request):
    return render(request, './home_finanzas.html')

@login_required
def boletas(request):
    data = {
        'boletas':listado_boleta()
    }
    print(listado_boleta())
    return render(request, './registro_boletas.html', data)

def listado_boleta():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_BOLETAS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

#
def total_boleta():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_BOLETAS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista