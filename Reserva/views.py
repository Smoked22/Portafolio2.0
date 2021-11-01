from django.shortcuts import redirect, render, redirect, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Mesa, Reserva, Cliente
from .forms import ReservaForm, ClienteForm
from .filters import ClienteFiltro
from django.db import connection
import cx_Oracle



#Inicio Reservas
@login_required
def home(request):
    return render(request, './home_reserva.html')

#Inicio Reservas
@login_required
def pruebas(request):
    return render(request, './prueba.html')


#Comenzar a hacer una reserva 
@login_required
def inicioReserva(request):
    return render(request, './inicioReserva.html')

#Listar Mesas
def mesas_listar(request):

    data = {
        #Almacena la variable para listar mesas
        'mesas' : listado_mesas()
    }
    return render(request,'./mesas_listado.html',data)



#Procedimiento Listar
def listado_mesas():
    django_cursor = connection.cursor()

    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    #Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    #Llamada al cursor 
    cursor.callproc("SP_LISTAR_MESAS", [out_cur])

    #llenamos la lista
    lista= []
    for fila in out_cur:
        lista.append(fila)
    return lista 

def listado_empleados():
    django_cursor = connection.cursor()

    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    #Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    #Llamada al cursor 
    cursor.callproc("SP_LISTAR_EMPLEADOS", [out_cur])

    #llenamos la lista
    lista= []
    for fila in out_cur:
        lista.append(fila)
    return lista 

def listado_mesas_disponibles():
    django_cursor = connection.cursor()

    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    #Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    #Llamada al cursor 
    cursor.callproc("SP_LISTAR_MESAS_DISPONIBLES", [out_cur])

    #llenamos la lista
    lista= []
    for fila in out_cur:
        lista.append(fila)
    return lista 

def listado_reservas_por_RUT(id):
    django_cursor = connection.cursor()

    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    #Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    #Llamada al cursor 
    cursor.callproc("SP_BUSCAR_RESERVA_POR_RUTCLI", [out_cur, id])

    #llenamos la lista
    lista= []
    for fila in out_cur:
        lista.append(fila)
    return lista 


def buscar_reserva(id):
    django_cursor = connection.cursor()

    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    #Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    #Llamada al cursor 
    cursor.callproc("SP_BUSCAR_RESERVA", [out_cur,id])

    #llenamos la lista
    lista= []
    for fila in out_cur:
        lista.append(fila)
    return lista 


def reserva_modificar(request,id):

    data = {
        'mesas' : listado_mesas_disponibles(),
        'empleados' : listado_empleados(),
        'reserva' : buscar_reserva(id)
    }

    if request.method== 'POST':
        fecha_reserva = request.POST.get('fecha_reserva')
        rut_emp = request.POST.get('empleado')
        rut_cli = request.POST.get('cliente')
        origen = request.POST.get('origen')
        id_mesa = request.POST.get('id_mesa')
        estado = request.POST.get('estado')
        cant = request.POST.get('cantP')

        salida = modificar_reserva( id, fecha_reserva, rut_emp, rut_cli, origen, id_mesa, estado, cant)

        if salida == 1:
            data['mensaje'] = 'agregador correctamente'
        else:
            data['mensaje'] = 'no se pudo guardar'

    return render(request, './reserva_modificar.html', data) 



def reserva_crear(request):

    data = {
        'mesas' : listado_mesas_disponibles(),
        'empleados' : listado_empleados(),
    }

    if request.method== 'POST':
        fecha_reserva = request.POST.get('fecha_reserva')
        rut_emp = request.POST.get('empleado')
        rut_cli = request.POST.get('cliente')
        origen = request.POST.get('origen')
        id_mesa = request.POST.get('id_mesa')
        estado = request.POST.get('estado')
        cant = request.POST.get('cantP')

        salida = crear_reserva( fecha_reserva, rut_emp, rut_cli, origen, id_mesa, estado, cant)

        if salida == 1:
            data['mensaje'] = 'agregador correctamente'
        else:
            data['mensaje'] = 'no se pudo guardar'

    return render(request, './reserva_crear.html', data) 


def crear_reserva( fecha_reserva, rut_emp, rut_cli, origen, id_mesa, estado, cant):
    django_cursor = connection.cursor()
    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_RESERVA',[fecha_reserva,rut_emp ,rut_cli ,origen ,id_mesa ,estado ,cant ,salida ])
    return salida.getvalue()

def modificar_reserva( ID,fecha_reserva, rut_emp, rut_cli, origen, id_mesa, estado, cant):
    django_cursor = connection.cursor()
    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_MODIFICAR_RESERVA',[ID, fecha_reserva,rut_emp ,rut_cli ,origen ,id_mesa ,estado ,cant ,salida ])
    return salida.getvalue()

def eliminar_reserva( id ):
    django_cursor = connection.cursor()
    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ELIMINAR_RESERVA',[id , salida ])
    return salida.getvalue()

def reserva_eliminar(request, id):

    data = {
        'mesas' : listado_mesas_disponibles(),
        'empleados' : listado_empleados(),
     
    }
   
    salida = eliminar_reserva(id)

    if salida == 1:
        data['mensaje'] = 'Borrado correctamente'
        data['reservas'] = listado_Reservas()
    else:
        data['mensaje'] = 'No se pudo borrar'
        data['reservas'] = listado_Reservas()

    

    return render(request, './reserva_listado.html', data)

def reserva_buscar(request, id):

    listadoReserva = listado_reservas_por_RUT(id)

    data = {
        'mesas' : listado_mesas_disponibles(),
        'empleados' : listado_empleados(),
        'reservas' : listadoReserva
     
    }    

    return render(request, './reserva_listado.html', data) 

#Listado reservas cursor
def listado_Reservas():
    django_cursor = connection.cursor()
    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    #Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_RESERVAS", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)
    return lista 



#Vista listado reserva
def reserva_listado(request):
    data = {
        'reservas' : listado_Reservas()
    }
    return render(request,'./reserva_listado.html',data)

