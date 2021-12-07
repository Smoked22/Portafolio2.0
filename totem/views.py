from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, redirect, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
import cx_Oracle
from django.db import connection
import datetime

# Create your views here.
# Inicio Reservas


@login_required
def home_totem(request):
    data = {
    }

    return render(request, './inicio_totem.html')

def totem_mensaje(request):
    data = {
    }

    return render(request, './mensaje.html')


def totem_login(request):
    data = {
    }
    
    if request.method == 'POST':
            rutsinmod = request.POST.get('rutCli')
            rut = rutsinmod[:-1]
            dv = rutsinmod[-1]
            nombre = 'John Doe'
            telefono = '00000000'
            correo = 'default@default.com'

            salida = crear_cliente(rut, dv, nombre, telefono, correo)

            if salida == 1:
                return mesas_listar(request, rut)
            else:
                return mesas_listar(request, rut)
    else:
        return render(request, './ingreso.html')


def crear_cliente(rut, dv, nom, telefono, correo):
    django_cursor = connection.cursor()
    # Cursor que llama
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_CLIENTE', [
                    rut, dv, nom, telefono, correo, salida])
    return salida.getvalue()


def mesas_listar(request, rut):

    cli = buscar_cliente(rut)

    data = {
        # Almacena la variable para listar mesas
        'mesas': listado_mesas(),
        'ruto': cli
    }

    return render(request, './home_totem.html', data)


def buscar_cliente(id):
    django_cursor = connection.cursor()
    # Cursor que llama
    cursor = django_cursor.connection.cursor()
    # Cursor que recibe
    out_cur = django_cursor.connection.cursor()
    # Llamada al cursor
    cursor.callproc("SP_CLI_POR_RUTCLI", [out_cur, id])
    # llenamos la lista
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def listado_mesas():
    django_cursor = connection.cursor()

    # Cursor que llama
    cursor = django_cursor.connection.cursor()
    # Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    # Llamada al cursor
    cursor.callproc("SP_LISTAR_MESAS_DISPONIBLES", [out_cur])

    # llenamos la lista
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def buscar_mesa(id):
    django_cursor = connection.cursor()

    # Cursor que llama
    cursor = django_cursor.connection.cursor()
    # Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    # Llamada al cursor
    cursor.callproc("SP_BUSCAR_MESA", [out_cur, id])

    # llenamos la lista
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista



def reservar_totem(request, id, sec):

    data = {
        'rut': buscar_cliente(id),
        'mesa': buscar_mesa(sec),
        'fecha': dameFecha()
    }

    if request.method == 'POST':

        rut_cli = request.POST.get('cliente')
        id_mesa = request.POST.get('id_mesa')
        cant = request.POST.get('cantP')

        salida = crear_reserva(rut_cli, id_mesa, cant)

        if salida == 1:
            return totem_mensaje(request)
        else:
            return totem_mensaje(request)

    return render(request, 'reserva.html', data)


def crear_reserva(rut_cli, id_mesa, cant):
    django_cursor = connection.cursor()
    # Cursor que llama
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_RESERVA_TOTEM', [rut_cli, id_mesa, cant, salida])
    return salida.getvalue()


def hora(request):
    ahora = datetime.datetime.now()
    hora = ahora.hour
    return hora

def dameFecha():
    x = datetime.datetime.now()
    fecha = (x.strftime("%x"))
    return fecha
