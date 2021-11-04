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


def cliente_listado(request):

    data = {
        'clientef' : listado_clientes(),
        'cliente' : listado_clientes()
    }

    if request.method== 'POST':
        id = request.POST.get('rutcli')
        listadofiltro = buscar_cliente(id)
        data['cliente'] = listadofiltro

    return render(request, './cliente_listar.html',data)


#Comenzar a hacer una reserva 
@login_required
def inicioReserva(request):
    return render(request, './cliente_listar.html')

#Listar Mesas
def mesas_listar(request):

    data = {
        #Almacena la variable para listar mesas
        'mesas' : listado_mesas()
    }
    return render(request,'./mesas_listado.html',data)


def listado_clientes():
    django_cursor = connection.cursor()

    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    #Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    #Llamada al cursor 
    cursor.callproc("SP_LISTAR_CLIENTES", [out_cur])

    #llenamos la lista
    lista= []
    for fila in out_cur:
        lista.append(fila)
    return lista 

#Procedimiento Listar
def listado_mesas():
    django_cursor = connection.cursor()

    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    #Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    #Llamada al cursor 
    cursor.callproc("SP_LISTAR_MESAS_DISPONIBLES_AHORA", [out_cur])

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

def buscar_cliente(id):
    django_cursor = connection.cursor()

    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    #Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    #Llamada al cursor 
    cursor.callproc("SP_BUSCAR_CLIENTE", [out_cur,id])

    #llenamos la lista
    lista= []
    for fila in out_cur:
        lista.append(fila)
    return lista 

def buscar_mesa(id):
    django_cursor = connection.cursor()

    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    #Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    #Llamada al cursor 
    cursor.callproc("SP_BUSCAR_MESA", [out_cur,id])

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

def cliente_modificar(request,id):

    data = {

        'cliente' : buscar_cliente(id)
    }

    if request.method== 'POST':
        rut = request.POST.get('rutCli')
        dv = request.POST.get('dv')
        nombre = request.POST.get('nom')
        telefono = int(request.POST.get('telefono'))
        correo = request.POST.get('correo')

        salida = modificar_cliente( rut,dv,nombre,telefono,correo)

        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
        else:
            data['mensaje'] = 'no se pudo guardar'

    return render(request, './cliente_modificar.html', data) 

def reserva_crear(request):

    data = {
        'mesas' : listado_mesas_disponibles(),
        'empleados' : listado_empleados(),
    }

    if request.method== 'POST':
        fecha_reserva = request.POST.get('fecha_reserva')
        hora_reserva = request.POST.get('hora_reserva')
        espacio = ' '
        fecha_hora = str(fecha_reserva)+espacio+str(hora_reserva)
        rut_emp = request.POST.get('empleado')
        rut_cli = request.POST.get('cliente')
        origen = 'Presencial'
        id_mesa = request.POST.get('id_mesa')
        estado = request.POST.get('estado')
        cant = request.POST.get('cantP')

        salida = crear_reserva( fecha_hora, rut_emp, rut_cli, origen, id_mesa, estado, cant)

        if salida == 1:
            data['mensaje'] = 'agregador correctamente'
        else:
            data['mensaje'] = 'no se pudo guardar'

    return render(request, './reserva_crear.html', data) 

def cliente_crear(request):

    data = {
        
    }

    if request.method== 'POST':

        rut = request.POST.get('rutCli')
        dv = request.POST.get('dv')
        nombre = request.POST.get('nom')
        telefono = int(request.POST.get('telefono'))
        correo = request.POST.get('correo')

        salida = crear_cliente( rut,dv,nombre,telefono,correo)

        if salida == 1:
            data['mensaje'] = 'agregador correctamente'
        else:
            data['mensaje'] = 'no se pudo guardar'

    return render(request, './cliente_crear.html', data) 


def crear_cliente( rut, dv, nom, telefono, correo):
    django_cursor = connection.cursor()
    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_CLIENTE',[rut, dv, nom, telefono, correo ,salida ])
    return salida.getvalue()

def modificar_cliente( rut, dv, nom, telefono, correo):
    django_cursor = connection.cursor()
    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_MODIFICAR_CLIENTE',[rut, dv, nom, telefono, correo ,salida ])
    return salida.getvalue()

def eliminar_cliente( rut ):
    django_cursor = connection.cursor()
    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ELIMINAR_CLIENTE',[rut, salida ])
    return salida.getvalue()


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

def cliente_eliminar(request, id):

    data = {
     
    }
   
    salida = eliminar_cliente(id)

    if salida == 1:
        data['mensaje'] = 'Borrado correctamente'
        data['cliente'] = listado_clientes()
    else:
        data['mensaje'] = 'No se pudo borrar'
        data['cliente'] = listado_clientes()

    return render(request, './cliente_listar.html', data)

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

def reserva_buscar(request):

    data = {
        'mesas' : listado_mesas_disponibles(),
        'empleados' : listado_empleados(),
    }

    if request.method== 'POST':
        id = request.POST.get('rutCli')
        listadoReserva = listado_reservas_por_RUT(id)

        data['mensaje'] = 'agregador correctamente'
        data['reservas'] = listadoReserva
    else:
        data['mensaje'] = 'no se pudo guardar'
        data['reservas'] = listado_Reservas()

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
        'reservas' : listado_Reservas(),
        'base' : listado_Reservas()
    }

    if request.method== 'POST':
        id = request.POST.get('rutcli')
        listadofiltro = listado_reservas_por_RUT(id)
        data['reservas'] = listadofiltro

    return render(request,'./reserva_listado.html',data)


def horario_mesa(request, id):
    data = {
        'horarios' :    listado_Horario(id),
        'mesa' :buscar_mesa(id)
    }

    return render(request,'./mesa_horario.html',data)

def listado_Horario(id):
    django_cursor = connection.cursor()
    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    #Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_HORARIO", [out_cur, id])

    lista= []
    for fila in out_cur:
        lista.append(fila)
    return lista 






