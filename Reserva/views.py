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




def reserva_crear(request):

    data = {
        'mesas' : listado_mesas(),
    }

    if request.method== 'POST':
        fecha_reserva = request.POST.get('fecha_reserva')
        fecha_hecha = request.POST.get('fecha_reserva_hecha')
        rut_emp = request.POST.get('empleado')
        rut_cli = request.POST.get('cliente')
        origen = request.POST.get('origen')
        id_mesa = request.POST.get('id_mesa')
        estado = request.POST.get('estado')
        cant = request.POST.get('cantP')

        salida = crear_reserva( fecha_reserva, fecha_hecha, rut_emp, rut_cli, origen, id_mesa, estado, cant)

        if salida == 1:
            data['mensaje'] = 'agregador correctamente'
        else:
            data['mensaje'] = 'no se pudo guardar'

    return render(request, './reserva_crear.html', data) 


def crear_reserva( fecha_reserva, fecha_hecha, rut_emp, rut_cli, origen, id_mesa, estado, cant):
    django_cursor = connection.cursor()
    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_RESERVA',[fecha_reserva ,fecha_hecha ,rut_emp ,rut_cli ,origen ,id_mesa ,estado ,cant ,salida ])
    return salida.getvalue()



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

