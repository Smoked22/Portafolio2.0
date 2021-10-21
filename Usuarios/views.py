from django.shortcuts import redirect, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Finanzas import urls
from .models import Ingrediente,Cliente, Carta, GuiaDesp, Suministro

#from .forms import formLog

@login_required
def home(request):
    return render(request, './home.html')

@login_required
def listarProductos(request):
    #Consulta y realiza una instancia a una lista de ingredientes
    ingredientes = Ingrediente.objects.all()
    #Diccionario
    data = {
        'ingredientes' : ingredientes
    }
    return render(request, './productosListado.html',data)

#def home_finanzas(request):
#    return render(request, './home_finanzas.html')

def acceder(request):
    #comprobar si es una peticion "POST"
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contra)
            if usuario is None:
                #login(request, usuario)
                #return redirect("home")
                messages.add_message(request, level=messages.ERROR, message="Usuario incorrecto")
            else:
                login(request, usuario)
                #switch (usuario.groups.filter)
                #switch no existe en Python, asi que se utilisa elif :c
                if usuario.groups.filter(name='Administrador').exists():
                    return redirect ("home")
                elif usuario.groups.filter(name='Finanzas').exists():
                    return redirect ("homefinanzas")
        else:
            messages.add_message(request, level=messages.ERROR, message="Los datos son incorrectos")

    form = AuthenticationForm()
    return render(request, "./index.html", {"form": form})


