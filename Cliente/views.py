from django.db import connection
from django.shortcuts import render
import cx_Oracle

# Create your views here.

def Cliente(request):
    return render(request, './home_cliente.html')

def ClienteEnMesa(request):
    return render(request, './clienteenmesa.html')

def CancelarReserva(request):

    data = {
        'mesas' : listado_mesas_disponibles(),
        'empleados' : listado_empleados(),
    }

    if request.method== 'POST':
        fecha_reserva = request.POST.get('fecha_reserva')
        hora_reserva = request.POST.get('hora_reserva')
        espacio = ' '
        fecha_hora = str(fecha_reserva)+espacio+str(hora_reserva)
        rut_cli = request.POST.get('cliente')

        salida = eliminar_reserva(fecha_hora, rut_cli)

        print(fecha_hora, rut_cli)

        if salida == 1:
            data['mensaje'] = 'Reserva eliminada correctamente'
        else:
            data['mensaje'] = 'No se pudo eliminar la reserva'

    return render(request, './cancelarReserva.html', data)

def VerMenu(request,num):
    data ={
        'cartas' : listado_cartas(),
        'entradas' : listado_entradas(),
        'fondos' : listado_fondos(),
        'ensaladas' : listado_ensaladas(),
        'postres' : listado_postres(),
        'bebidas' : listado_bebidas()
    }

    if request.method== 'POST':
        cant = request.POST.get('cant')
        nom = request.POST.get('nom')
        if nom is not None or (nom == 0):
            str= buscar_id(nom)
            id_carta = "".join(''.join(elems) for elems in str)
            print(id_carta)
        else:
            id_carta='0'
        

        
        print(cant,id_carta,num)




    return render(request, './menu.html',data)



def buscar_id(nom):
    django_cursor = connection.cursor()
    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    #Cursor que recibe
    out_cur = django_cursor.connection.cursor()
    #Llamada al cursor 
    cursor.callproc("SP_BUSCAR_ID_CON_NOM", [nom,out_cur])
    #llenamos la lista
    lista= []
    for fila in out_cur:
        lista.append(fila)
    return lista




    

def MenuEntrada(request):
    data ={
        'entradas' : listado_entradas()
    }
    return render(request, './menu_Entrada.html',data)

def MenuFondo(request):
    data ={
        'fondos' : listado_fondos()
    }
    return render(request, './menu_Fondo.html',data)

def MenuEnsalada(request):
    data ={
        'ensaladas' : listado_ensaladas()
    }
    return render(request, './menu_Ensalada.html',data)

def MenuPostre(request):
    data ={
        'postres' : listado_postres()
    }
    return render(request, './menu_Postre.html',data)

def MenuBeber(request):
    data ={
        'bebidas' : listado_bebidas()
    }
    return render(request, './menu_Beber.html',data)

def Reservar(request):
    return render(request, './reservar.html')


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
        hora_reserva = request.POST.get('hora_reserva')
        espacio = ' '
        fecha_hora = str(fecha_reserva)+espacio+str(hora_reserva)
        rut_emp = 0
        rut_cli = request.POST.get('cliente')
        origen = 'Cliente'
        id_mesa = request.POST.get('id_mesa')
        estado = 'Reserva'
        cant = request.POST.get('cantP')

        salida = crear_reserva(fecha_hora, rut_emp, rut_cli, origen, id_mesa, estado, cant)

        if salida == 1:
            data['mensaje'] = 'Reserva agregada correctamente'
        else:
            data['mensaje'] = 'No se pudo guardar'

    return render(request, './reservarMesa.html', data)

def eliminar_reserva(fecha_hora, rut_cli):
    django_cursor = connection.cursor()
    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ELIMINAR_RESERVA_CLIENTE', [fecha_hora, rut_cli, salida])
    return salida.getvalue()

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

def listado_entradas():
    django_cursor = connection.cursor()
    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    #Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_ENTRADA", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)
    return lista

def listado_fondos():
    django_cursor = connection.cursor()
    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    #Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_FONDO", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)
    return lista

def listado_ensaladas():
    django_cursor = connection.cursor()
    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    #Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_ENSALADA", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)
    return lista

def listado_postres():
    django_cursor = connection.cursor()
    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    #Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_POSTRE", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)
    return lista

def listado_bebidas():
    django_cursor = connection.cursor()
    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    #Cursor que recibe
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_BEBIDA", [out_cur])

    lista= []
    for fila in out_cur:
        lista.append(fila)
    return lista


def ClienteCrear(request):

    data = {

    }

    if request.method == 'POST':

        rut = request.POST.get('rutCli')
        dv = request.POST.get('dv')
        nombre = request.POST.get('nom')
        telefono = int(request.POST.get('telefono'))
        correo = request.POST.get('correo')

        salida = CrearCliente(rut, dv, nombre, telefono, correo)

        if salida == 1:
            data['mensaje'] = 'Cliente agregado correctamente'
        else:
            data['mensaje'] = 'No se pudo agregar el cliente'

    return render(request, './crear_cliente.html', data)


def CrearCliente(rut, dv, nom, telefono, correo):
    django_cursor = connection.cursor()
    # Cursor que llama
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_CLIENTE', [rut, dv, nom, telefono, correo, salida])
    return salida.getvalue()


#Nueva sección
def MesaCliente(request):

    data = {
        'mesas' : listado_mesas()

    }

    return render(request, './seleccion_mesa.html', data)

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


def InicioMesa(request, id):

    data = {
        'mesa' : id
    }

    return render(request, './mesa_inicio.html', data)

def HomeMesa(request, id):
    data = {
        'mesa' : id,
        'entradas': listado_entradas(),
        'cartas' : listado_cartas(),
        'fondos' : listado_fondos(),
        'ensaladas' : listado_ensaladas(),
        'postres' : listado_postres(),
        'bebidas' : listado_bebidas()
    }
    if request.method == 'POST':
        frederic  = request.POST.get('datos')
        cantidad  = request.POST.get('cant')
        listderic = Convert(frederic)
        listdecant = Convert(cantidad)
        id_orden = crear_orden_detallada(id)

        for i in range(len(listderic)):
            
            id_carta = buscar_id_por_nom(listderic[i])
            cant = listdecant[i]
            salida = crear_detalle_orden(cant,id_orden,id_carta)

        salida = crear_orden_detallada(id)

    return render(request, './mesa_menu.html', data)

# Python code to convert string to list
def Convert(string):
    li = list(string.split(","))
    return li
    
   


def crear_orden_detallada(id):
    django_cursor = connection.cursor()
    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_CREAR_ORDEN_DETALLADA',[id,salida ])
    return salida.getvalue()

def crear_detalle_orden(cant,id_orden,id_carta):
    django_cursor = connection.cursor()
    #Cursor que llama
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_CREAR_DETALLE_ORDEN',[cant,id_orden,id_carta,salida ])
    return salida.getvalue()

def buscar_id_por_nom(nom):
    django_cursor = connection.cursor()

    # Cursor que llama
    cursor = django_cursor.connection.cursor()
    # Cursor que recibe
    salida = cursor.var(cx_Oracle.NCHAR)

    # Llamada al cursor
    cursor.callproc("SP_BUSCAR_CARTA_POR_NOM", [nom,salida])

    # llenamos la lista
    return salida.getvalue()


