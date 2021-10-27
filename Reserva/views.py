from django.shortcuts import redirect, render, redirect, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Mesa, Reserva
from .forms import ReservaForm, ClienteForm

# Create your views here.

@login_required
def home(request):
    return render(request, './home_reserva.html')


@login_required
def reservas(request):
    mesa = Mesa.objects.all()
    data = {
        'mesa' : mesa
    }
    return render(request, './reservas.html',data)

@login_required
def crearReserva(request):
    form_class = ReservaForm
    data = {
        'form': ReservaForm()
    }
    if request.method  == 'POST':
        formulario = ReservaForm(data=request.POST) 
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Reserva Guardada"
        else:
            data["form"] = formulario

    return render(request, './nuevaReserva.html',data)

@login_required
def crearCliente(request):
    form_class = ClienteForm
    data = {
        'form': ClienteForm()
    }
    if request.method  == 'POST':
        formulario = ClienteForm(data=request.POST) 
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Cliente Guardado"
        else:
            data["form"] = formulario

    return render(request, './nuevoCliente.html',data)



