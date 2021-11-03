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

#from .forms import formLog

@login_required
def home_admin(request):
    data = {
        'reservas' : reserva_info(),
  
    }
    return render(request, './home_admin.html', data)


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



