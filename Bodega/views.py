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
    return render(request, './home_bodega.html')

@login_required
def ingredientes(request):
    data = {
        'ingredientes':listado_ingredienter()
         
    }

    return render(request, './registro_ingrediente.html', data)


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


    if request.method == 'POST':
        ID_INGREDIENTE = request.POST.get('id_productos') 
        NOM_INGREDIENTE = request.POST.get('nombre_ingrediente') 
        DESC_INGREDIENTE = request.POST.get('categoria') 
        STOCK = request.POST.get('stock') 
        UNIDAD_DE_MEDIDA = request.POST.get('un_medida') 
        FEC_CADUC  = request.POST.get('fecha') 
        salida = ingresar_ingrediente(ID_INGREDIENTE, NOM_INGREDIENTE, DESC_INGREDIENTE, STOCK, UNIDAD_DE_MEDIDA, FEC_CADUC)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
        else:
            data['mensaje'] = 'no se ha agregado'
    return render(request, './agregar_ingrediente.html' , data)


# LISTAR LOS INGREDIENTES PARA MODFICAR
def modificar_ingrediente(request):
    
    data = {
        'categorias' :listar_categoria()
    }

    return render(request, './lista_ingredientemod.html' , data)


def ingresar_modificar_ingrediente(ID_INGREDIENTE, NOM_INGREDIENTE, DESC_INGREDIENTE, STOCK, UNIDAD_DE_MEDIDA, FEC_CADUC):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_MODIFICAR_INGREDIENTER',[ID_INGREDIENTE, NOM_INGREDIENTE, DESC_INGREDIENTE, STOCK, UNIDAD_DE_MEDIDA, FEC_CADUC, salida])
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


def eliminar_ingrediente( id ):
    django_cursor = connection.cursor()
    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ELIMINAR_INGREDIENTER',[id , salida ])
    return salida.getvalue()

def ingrediente_eliminar(request, id):

    data = {
        'categorias' :listar_categoria()
        
     
    }
   
    salida = eliminar_ingrediente(id)

    if salida == 1:
        data['mensaje'] = 'Borrado correctamente'
        data['categorias'] = listado_ingredienter()
    else:
        data['mensaje'] = 'No se pudo borrar'
        data['categorias'] = listado_ingredienter()

    

    return render(request, './lista_ingredientemod.html', data)    
    
def buscar_ingrediente(id):
    django_cursor = connection.cursor()

    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    #Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    #Llamada al cursor 
    cursor.callproc("SP_BUSCAR_INGREDIENTER", [out_cur,id])

    #llenamos la lista
    lista= []
    for fila in out_cur:
        lista.append(fila)
    return lista 

def buscar_ingrediente_lista(request, id):

    listadoReserva = buscar_ingrediente(id)

    data = {
    'categorias' : listar_categoria 
    # 'reservas' : listadoReserva
     
    }    

    return render(request, './lista_ingredientemod.html', data)

def modificar_ingrediente_rellenar(request, id):
    data= {

    'categorias' :listar_categoria()        
    }
    

    if request.method == 'POST':
        ID_INGREDIENTE = request.POST.get('id_productos') 
        NOM_INGREDIENTE = request.POST.get('nombre_ingrediente') 
        DESC_INGREDIENTE = request.POST.get('categoria') 
        STOCK = request.POST.get('stock') 
        UNIDAD_DE_MEDIDA = request.POST.get('un_medida') 
        FEC_CADUC  = request.POST.get('fecha') 
        salida = ingresar_modificar_ingrediente(ID_INGREDIENTE, NOM_INGREDIENTE, DESC_INGREDIENTE, STOCK, UNIDAD_DE_MEDIDA, FEC_CADUC)
        if salida == 1:
            data['mensaje'] = 'Modificado correctamente'
        else:
            data['mensaje'] = 'no se ha Modificado'
    return render(request, './modificar_ingrediente.html', data)

# METODO PARA LISTAR LOS INGREDIENTES
def listado_ingredienter():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_INGREDIENTER", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


# METODO PARA LISTADOSUMUNISTROS
def listar_suministro():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_SUMINISTROR", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


# METODO PARA LISTADOPROVEEDORES
def listar_proveedor():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PROVEEDORR", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

# METODO PARA AGREGAR UN INGREDIENTE
def ingresar_ingrediente(ID_INGREDIENTE, NOM_INGREDIENTE, DESC_INGREDIENTE, STOCK, UNIDAD_DE_MEDIDA, FEC_CADUC):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_PRODUCTOR',[ID_INGREDIENTE, NOM_INGREDIENTE, DESC_INGREDIENTE, STOCK, UNIDAD_DE_MEDIDA, FEC_CADUC, salida])
    return salida.getvalue()