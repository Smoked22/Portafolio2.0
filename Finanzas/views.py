from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db import connection

# Create your views here.

#creamos una funcion para renderizar la pagina home de finanzas
@login_required
def home_finanzas(request):
    return render(request, './home_finanzas.html')

#Creamos una funcion para renderizar "registro_boletas.html"
@login_required
def boletas(request):
    data = {
        'boletas':listado_boleta()
    }
    print(listado_boleta())
    return render(request, './registro_boletas.html', data)

#Creamos una funciona para llamar al procedimiento almacenado
def listado_boleta():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_BOLETAS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

#Funcion para renderizar la pagina "registro_proveedores.html"
@login_required
def proveedores(request):
    data = {
        'proveedores':listado_proveedor()
    }
    return render(request, './registro_proveedores.html',data)

#Creamos una funciona para llamar al procedimiento almacenado
def listado_proveedor():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PROVEEDORES", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista

#Funcion para renderizar la pagina "guias_despacho.html"
def guia_despacho(request):
    return render(request, './guias_despacho.html')

#Funcion para renderizar la pagina "guias_despacho.html"

#codigo prueba
