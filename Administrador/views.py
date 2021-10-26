from django.shortcuts import redirect, render, redirect, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Finanzas import urls
#from .models import Ingrediente , Cliente, Carta, GuiaDesp, Suministro
from .forms import IngredienteForm

#from .forms import formLog

@login_required
def home(request):
    return render(request, './home.html')


@login_required
def ingredientespage(request):
    return render(request, './ingrediente.html')

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



