from django.shortcuts import redirect, render, redirect, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Finanzas import urls
from .models import Ingrediente , Cliente, Carta, GuiaDesp, Suministro
from .forms import IngredienteForm
from django.db import connection
from django.http import JsonResponse
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
import cx_Oracle
from datetime import date, timedelta,datetime
import datetime
import locale

#from .forms import formLog

@login_required
def home_admin(request):
    data = {
        'reservas' : reserva_info(),
        'empleados' : empleados_info()
  
    }
    return render(request, './home_admin.html', data)



def informe_reservas(request):
    return render(request, './Reserva_Grafico.html')


def grafico_reserva(request):

    hoy = date.today()
    nohoy = hoy - timedelta(days = 0)
    nohoy = nohoy.strftime("%A")

    #LABELS PASADO
    ayer = hoy - timedelta(days = 1)
    ayer = ayer.strftime("%A")

    anteayer = hoy   - timedelta(days = 2)
    anteayer = anteayer.strftime("%A")

    antiayer = hoy - timedelta(days = 3)
    antiayer = antiayer.strftime("%A")

    #EL FUTURO ES HOY OISTE VIEJO
    manana= hoy + timedelta(days = 1)
    manana = manana.strftime("%A")

    pasadomanana = hoy + timedelta(days = 2)
    pasadomanana = pasadomanana.strftime("%A")

    postmanana = hoy + timedelta(days = 3)
    postmanana = postmanana.strftime("%A")

    nombres = []
    nombres.append(antiayer)
    nombres.append(anteayer)
    nombres.append(ayer)
    nombres.append(nohoy)
    nombres.append(manana)
    nombres.append(pasadomanana)
    nombres.append(postmanana)

    b = grafico_reserva_base()
    data = []
    data = b[0]
    
    return JsonResponse(data={
        'data': data,
        'labels': nombres
    })



def grafico_reserva_base():
    django_cursor = connection.cursor()
    # Cursor que llama
    cursor = django_cursor.connection.cursor()
    # Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_GRAFICO_DATA_RESERVA_DIAS_2", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista



@login_required
def ingredientespage(request):
    return render(request, './ingrediente.html')

def detalle_empleado(request,id):

    data = {
        'empleado' : buscar_empleado(id)
    }


    return render(request, './detalle_empleado.html',data)

def empleados(request):
    data ={
        'empleados' : empleados_info()
    }
    return render(request, './listado_empleados.html',data)

#Procedimiento Listar
def reserva_info():
    django_cursor = connection.cursor()

    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    #Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    #Llamada al cursor 
    cursor.callproc("SP_BUSCAR_INFO_RESERVAS", [out_cur])

    #llenamos la lista
    lista= []
    for fila in out_cur:
        lista.append(fila)
    return lista 

def empleados_info():
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

def buscar_empleado(id):
    django_cursor = connection.cursor()

    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    #Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    #Llamada al cursor 
    cursor.callproc("SP_BUSCAR_EMPLEADO", [out_cur, id])

    #llenamos la lista
    lista= []
    for fila in out_cur:
        lista.append(fila)
    return lista    


@login_required
def modificarProductos(request, id):

    ingrediente = get_object_or_404(Ingrediente, id_ingrediente=id)

    data = {
        'form': IngredienteForm(instance=ingrediente)
    }

    if request.method == 'POST':
        formulario = IngredienteForm(data=request.POST, instance=ingrediente)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarProductos")
        data["form"] = formulario


    return render(request, './modificarIngrediente.html', data)

@login_required
def listarProductos(request):
    #Consulta y realiza una instancia a una lista de ingredientes
    ingredientes = Ingrediente.objects.all()
    #Diccionario
    data = {
        'ingredientes' : ingredientes
    }
    return render(request, './productosListado.html',data)

@login_required
def crearProductos(request):
    form_class = IngredienteForm
    data = {
        'form': IngredienteForm()
    }
    if request.method  == 'POST':
        formulario = IngredienteForm(data=request.POST) 
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Ingrediente Guardado"
        else:
            data["form"] = formulario

    return render(request, './CrearProducto.html',data)

#parte Reservas

def listado_Reservas_admin():
    django_cursor = connection.cursor()
    # Cursor que llama
    cursor = django_cursor.connection.cursor()
    # Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_RESERVAS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


# Vista listado reserva
def listar_reservas_admin(request):
    data = {
        'reservas': listado_Reservas_admin(),
    }

    return render(request, './listar_reservas_admin.html', data)

    # Vista listado reserva detalle
def listar_reservas_detalle_admin(request):
    data = {
        'reservas': listado_Reservas_admin(),
    }

    return render(request, './listado_reserva_detalle_admin.html', data)

#crear reserva 
def enviar_reserva_admin(fecha_reserva, rut_emp, rut_cli, origen, id_mesa, estado, cant):
    django_cursor = connection.cursor()
    # Cursor que llama
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_RESERVA', [
                    fecha_reserva, rut_emp, rut_cli, origen, id_mesa, estado, cant, salida])
    return salida.getvalue()

def crear_reservas_admin(request):

    data = {
        'mesas': listado_mesas_disponibles(),
        'empleados': listado_empleados(),
    }

    if request.method == 'POST':
        fecha_reserva = request.POST.get('fecha_reserva')
        hora_reserva = request.POST.get('hora_reserva')
        espacio = ' '
        fecha_hora = str(fecha_reserva)+espacio+str(hora_reserva)
        rut_emp = request.POST.get('empleado')
        rut_cli = request.POST.get('cliente')
        origen = 'PRESENCIAL'
        id_mesa = request.POST.get('id_mesa')
        estado = 'RESERVADA'
        cant = request.POST.get('cantP')

        salida = enviar_reserva_admin(fecha_hora, rut_emp, rut_cli,
                               origen, id_mesa, estado, cant)

        if salida == 1:
            messages.success(request, "Reserva Creada")
        else:
            messages.error(request, "No se pued crear la reserva")

    return render(request, './crear_reservas_admin.html', data)

def listado_mesas_disponibles():
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


#LISTADO EMPLEADO
def listado_empleados():
    django_cursor = connection.cursor()

    # Cursor que llama
    cursor = django_cursor.connection.cursor()
    # Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    # Llamada al cursor
    cursor.callproc("SP_LISTAR_EMPLEADOS", [out_cur])

    # llenamos la lista
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


#AREA CLIENTE
def cliente_crear(request):
    data = {
    }
    if request.method == 'POST':

        rut = request.POST.get('rutCli')
        dv = request.POST.get('dv')
        nombre = request.POST.get('nom')
        telefono = int(request.POST.get('telefono'))
        correo = request.POST.get('correo')

        salida = crear_cliente(rut, dv, nombre, telefono, correo)

        if salida == 1:
            messages.success(request, "Cliente ha sido creado")
        else:
            messages.error(request, "El cliente no ha podido crearse")

    return render(request, './cliente_crear_admin.html', data)

def cliente_listado(request):
    data = {
        'clientef': listado_clientes(),
        'cliente': listado_clientes()
    }
    if request.method == 'POST':
        id = request.POST.get('rutcli')
        listadofiltro = buscar_cliente(id)
        data['cliente'] = listadofiltro

    return render(request, './cliente_listar_admin.html', data)

def listado_clientes():
    django_cursor = connection.cursor()
    # Cursor que llama
    cursor = django_cursor.connection.cursor()
    # Cursor que recibe
    out_cur = django_cursor.connection.cursor()
    # Llamada al cursor
    cursor.callproc("SP_LISTAR_CLIENTES", [out_cur])
    # llenamos la lista
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def buscar_cliente(id):
    django_cursor = connection.cursor()
    # Cursor que llama
    cursor = django_cursor.connection.cursor()
    # Cursor que recibe
    out_cur = django_cursor.connection.cursor()
    # Llamada al cursor
    cursor.callproc("SP_BUSCAR_CLIENTE", [out_cur, id])
    # llenamos la lista
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista



def cliente_modificar(request, id):
    data = {
        'cliente': buscar_cliente(id)
    }
    if request.method == 'POST':
        rut = request.POST.get('rutCli')
        dv = request.POST.get('dv')
        nombre = request.POST.get('nom')
        telefono = int(request.POST.get('telefono'))
        correo = request.POST.get('correo')
        salida = modificar_cliente(rut, dv, nombre, telefono, correo)

        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
        else:
            data['mensaje'] = 'no se pudo guardar'
    return render(request, './cliente_modificar_admin.html', data)


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
    return render(request, './cliente_listar_admin.html', data)


def crear_cliente(rut, dv, nom, telefono, correo):
    django_cursor = connection.cursor()
    # Cursor que llama
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_CLIENTE', [
                    rut, dv, nom, telefono, correo, salida])
    return salida.getvalue()


def modificar_cliente(rut, dv, nom, telefono, correo):
    django_cursor = connection.cursor()
    # Cursor que llama
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_MODIFICAR_CLIENTE', [
                    rut, dv, nom, telefono, correo, salida])
    return salida.getvalue()


def eliminar_cliente(rut):
    django_cursor = connection.cursor()
    # Cursor que llama
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ELIMINAR_CLIENTE', [rut, salida])
    return salida.getvalue()




