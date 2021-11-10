from django.db import connection
from django.shortcuts import render
import cx_Oracle

# Create your views here.

def Cliente(request):
    return render(request, './home_cliente.html')

def ClienteEnMesa(request):
    return render(request, './clienteenmesa.html')

def CancelarReserva(request):
    return render(request, './cancelarReserva.html')

def VerMenu(request):
    data ={
        'cartas' : listado_cartas()
    }
    return render(request, './menu.html',data)

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

def ReservarMesa(request):

    data = {
        'mesas' : listado_mesas_disponibles(),
        'empleados' : listado_empleados(),
    }

    if request.method== 'POST':
        fecha_reserva = request.POST.get('fecha_reserva')
        rut_emp = request.POST.get('empleado')
        rut_cli = request.POST.get('cliente')
        origen = 'Cliente'
        id_mesa = request.POST.get('id_mesa')
        estado = 'Reserva'
        cant = request.POST.get('cantP')

        salida = crear_reserva(fecha_reserva, rut_emp, rut_cli, origen, id_mesa, estado, cant)

        if salida == 1:
            data['mensaje'] = 'Reserva agregada correctamente'
        else:
            data['mensaje'] = 'No se pudo guardar'

    return render(request, './reservarMesa.html', data)

def crear_reserva( fecha_reserva, rut_emp, rut_cli, origen, id_mesa, estado, cant):
    django_cursor = connection.cursor()
    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_RESERVA',[fecha_reserva,rut_emp ,rut_cli ,origen ,id_mesa ,estado ,cant ,salida ])
    return salida.getvalue()

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

