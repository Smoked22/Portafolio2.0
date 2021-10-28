from django.shortcuts import render

# Create your views here.

def Cliente(request):
    return render(request, './home_cliente.html')

def ClienteEnMesa(request):
    return render(request, './clienteenmesa.html')