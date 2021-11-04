from django.shortcuts import redirect, render, redirect, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
import cx_Oracle
# Create your views here.

@login_required
def home(request):
    return render(request, './home_cocina.html')

@login_required
def receta(request):
    data = {
        'recetas':listado_ingredienter()
    }

    return render(request, './registro_receta.html', data)

def receta_crear(request):
    
    data = {
        'carta' :listado_cartas()
    }

    if request.method == 'POST':

        nome = request.POST.get('nom') 
        desce = request.POST.get('desc') 
        porcione = request.POST.get('porcion') 
        cartae = request.POST.get('carta')

        salida = agregar_receta( nome, desce, porcione,cartae)

        if salida == 1:
            data['mensaje'] = 'Agregado correctamente'
        else:
            data['mensaje'] = 'No se ha agregado'

    return render(request, './crear_receta.html' , data)

#Listado reservas cursor
def listado_cartas():
    django_cursor = connection.cursor()
    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    #Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_CARTA", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)
    return lista 

def agregar_receta( nom, desc, porcion, carta):
    django_cursor = connection.cursor()
    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_RECETA_D',[nom, desc , porcion, carta, salida] )
    return salida.getvalue()


def listar_recetas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_CARTA_DETALLE", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def receta_listado(request):
    data = {
        'receta': listar_recetas()
    }

    return render(request,'./listar_recetas.html',data)


# LISTAR LAS RECETAS PARA MODFICAR
def modificar_receta(request):
    
    data = {
        'categorias' :listar_categoria()
    }

    return render(request, './lista_recetamod.html' , data)


def ingresar_modificar_receta(ID_RECETA, NOM_RECETA, DESC_RECETA, PORCION, CARTA_ID_CARTA):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_MODIFICAR_RECETAR',[ID_RECETA, NOM_RECETA, DESC_RECETA, PORCION, CARTA_ID_CARTA, salida])
    return salida.getvalue()


def proveedor(request):
    data = {
        'proveedor':listar_proveedor()
    }

    return render(request, './listar_proveedores.html', data)


def suministro(request):
    data = {
        'suministro':listar_suministro() 
    }
    return render(request, './listar_suministros.html', data)


def eliminar_receta( id ):
    django_cursor = connection.cursor()
    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ELIMINAR_RECETAR',[id , salida ])
    return salida.getvalue()

def receta_eliminar(request, id):

    data = {
        'categorias' :listar_categoria()
        
     
    }
   
    salida = eliminar_reserva(id)

    if salida == 1:
        data['mensaje'] = 'Borrado correctamente'
        data['reservas'] = listadoReserva()
    else:
        data['mensaje'] = 'No se pudo borrar'
        data['reservas'] = listadoReserva()

    

    return render(request, './lista_recetamod.html', data)    
    
def buscar_receta(id):
    django_cursor = connection.cursor()

    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    #Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    #Llamada al cursor 
    cursor.callproc("SP_BUSCAR_RECETAR", [out_cur,id])

    #llenamos la lista
    lista= []
    for fila in out_cur:
        lista.append(fila)
    return lista 

def buscar_receta_lista(request, id):

    listadoReserva = buscar_receta(id)

    data = {
    'categorias' : listar_categoria 
     
    }    

    return render(request, './lista_recetamod.html', data)

def modificar_orden_rellenar(request):
    data= {

    'categorias' :listar_categoria()        
    }
    

    if request.method == 'POST':
        ID_ORDEN = request.POST.get('id_orden') 
        FECHA = request.POST.get('fecha') 
        HORA = request.POST.get('hora') 
        MESA_ID_MESA = request.POST.get('mesa_id_mesa') 
        salida = ingresar_ingrediente(ID_ORDEN, FECHA, HORA, MESA_ID_MESA)
        if salida == 1:
            data['mensaje'] = 'Modificado correctamente'
        else:
            data['mensaje'] = 'no se ha Modificado'
    return render(request, './modificar_ordenes.html', data)






#LISTAR ORDENES
def listado_ordenes():
    django_cursor = connection.cursor()

    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    #Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    #Llamada al cursor 
    cursor.callproc("SP_LISTAR_ORDEN", [out_cur])

    #llenamos la lista
    lista= []
    for fila in out_cur:
        lista.append(fila)
    return lista 

def orden_listado(request):
    data = {
        'ordenes':listado_ordenes()
    }
    return render(request, './ordenes_listado.html', data)


def orden_detalle(request, id):
    
    data = {
        'ordenes' : detalles_ordenes(id)
    }

    return render(request, './detalle_orden.html', data)


def detalles_ordenes(id):
    django_cursor = connection.cursor()
    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    #Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    #Llamada al cursor 
    cursor.callproc("SP_LISTAR_DETALLE_ORDEN_2", [out_cur, id])

    #llenamos la lista
    lista= []
    for fila in out_cur:
        lista.append(fila)
    return lista 

def orden_actualizar(request, id, sec, sec2):
    
    actualizar_ordenes(id, sec, sec2)

    data = {
        'ordenes': detalles_ordenes(id)
        
    }

    return render(request, './detalle_orden.html', data)

def actualizar_ordenes(id,sec, sec2):
    django_cursor = connection.cursor()
    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_MODIFICAR_ORDENES',[id, sec , sec2 ,salida ])
    return salida.getvalue()
    


