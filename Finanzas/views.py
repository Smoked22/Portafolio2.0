from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db import connection
import cx_Oracle

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
#Funciona para renderizar la pagina "ingresar_boleta.html"
def agegar_boleta(request):
    data = {
    }
    print(listado_boleta())
    ingresar_boleta('40','24-09-2021','14:20','12000','Transferencia','13')
    #si es un metodo "POST" entra en el if
    if request.method == 'POST':
        id_boleta = request.POST.get('id_boleta')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        monto = request.POST.get('monto')
        tipo_pago = request.POST.get('tipo_pago')
        id_orden = request.POST.get('id_orden')  

        #problema con el procedimiento almacenado, al momento de enviar los datos se queda cargando la pagina y ahi queda :C
        salida = ingresar_boleta(id_boleta, fecha, hora, monto, tipo_pago, id_orden)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
        else:
            data['mensaje'] = 'no se ha agregado'

    return render(request, './ingresar_boleta.html', data)

#Creamos una funcion para llamar el procedimiento almacenado
def ingresar_boleta(id_boleta, fecha, hora, monto, tipo_pago, id_orden):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_BOLETA',[id_boleta,fecha, hora, monto, tipo_pago,id_orden, salida])
    return salida.getvalue()

#Funcion para renderizar la pagina "registro_proveedores.html"
@login_required
def proveedores(request):
    data = {
        'proveedores':listado_proveedor()
    }
    print(listado_proveedor())
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
    data = {
        'guia_despacho':listado_guia_despacho
    }
    return render(request, './guias_despacho.html', data)

#Funcion para renderizar la pagina "guias_despacho.html"
def listado_guia_despacho():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_GUIAS_DESPACHO", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista
#codigo prueba
