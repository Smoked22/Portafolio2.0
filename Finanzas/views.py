from typing_extensions import Required
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db import connection
from django.contrib import messages
import cx_Oracle

# Create your views here.

# creamos una funcion para renderizar la pagina home de finanzas

@login_required
def home_finanzas(request):
    data = {
        'ventas_dias': ventas_semana(),
    }
    print(ventas_semana())
    return render(request, './home_finanzas.html', data)

# Creamos un procedimiento almacenado para mostrar las ventas de los dias anteriores

def ventas_semana():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_VENTA_SEMANA", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

# Creamos una funcion para renderizar "registro_boletas.html"

@login_required
def boletas(request):
    data = {
        'boletas': listado_boleta()
    }
    return render(request, './registro_boletas.html', data)

# Creamos una funciona para llamar al procedimiento almacenado

def listado_boleta():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_BOLETAS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


# Funciona para renderizar la pagina "ingresar_boleta.html"
@login_required
def agegar_boleta(request):
    data = {
        'orden_disp':listar_orden_disp()
    }

    # si es un metodo "POST" entra en el if
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        fechaprueba = request.POST.get('anio2')
        print(fechaprueba)
        print(fecha)
        hora = request.POST.get('hora')
        monto = request.POST.get('monto')
        tipo_pago = request.POST.get('tipo_pago')
        id_orden = request.POST.get('id_orden')

        # problema con el procedimiento almacenado, al momento de enviar los datos se queda cargando la pagina y ahi queda :C
        # se cancela, si esta funcionando la wea, anoche tenai sue??o el django y no queria funcionar
        salida = ingresar_boleta(
             fecha, hora, monto, tipo_pago, id_orden)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
            return redirect(boletas)
        else:
            data['mensaje'] = 'no se ha agregado'


    return render(request, './ingresar_boleta.html', data)


# Creamos una funcion para llamar el procedimiento almacenado

def ingresar_boleta( fecha, hora, monto, tipo_pago, id_orden):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_BOLETA2', [
                     fecha, hora, monto, tipo_pago, id_orden, salida])
    return salida.getvalue()


#Creamos procedimiento almacenado para listar la ordenes disponibles

def listar_orden_disp():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_ORDENES_LIBRES", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def id_de_boleta():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_PUESTO_BOLETA", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

# Funcion para renderizar la pagina "registro_proveedores.html"

@login_required
def proveedores(request):
    data = {
        'proveedores': listado_proveedor()
    }
    # print(listado_proveedor())
    return render(request, './registro_proveedores.html', data)


# Creamos una funciona para llamar al procedimiento almacenado

def listado_proveedor():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PROVEEDORES", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


# Funcion para renderizar la pagina "Producto_proveedores.html"

@login_required
def listado_produc_proveedor(request, id):
    data = {
        'producto': lista_productos(id),
    }
    return render(request, './productos_proveedores.html', data)


# Procedimiento almacenado "Listar productos de proveedores"

def lista_productos(rut):
    django_cursor = connection.cursor()

    cursor = django_cursor.connection.cursor()

    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PRODUCTOS_PROVEEDORES", [out_cur, rut])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


# Funcion para renderizar la pagina "guias_despacho.html"

@login_required
def guia_despacho(request):
    data = {
        'guia_despacho': listado_guia_despacho
    }
    return render(request, './guias_despacho.html', data)


# Procedimiento almacenado "Listar guias de despacho"

def listado_guia_despacho():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_GUIAS_DESPACHO", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

# Renderizar pagina prueba
@login_required
def grafico(request):
    data = {
        'datos_grafico': datos_grafico,
        'ventas_dias': ventas_semana
    }
    return render(request,'./graficos.html',data)

def datos_grafico():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_MONTO_MENSUAL", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista
# codigo prueba

def prueba(request):
    data = {
        'boletas': listado_boleta()
    }
    return render(request,'./prueba.html', data)

def prueba2(request):
    data = {
    }
    return render(request,'./prueba2.html', data)
