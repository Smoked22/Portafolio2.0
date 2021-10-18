from django.shortcuts import redirect, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#from .forms import formLog

@login_required
def home(request):
    return render(request, './home.html')

def acceder(request):
    #comprobar si es una peticion "POST"
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect("home")
            else:
                messages.add_message(request, level=messages.ERROR, message="Usuario incorrecto")
        else:
            messages.add_message(request, level=messages.ERROR, message="Los datos son incorrectos")

    form = AuthenticationForm()
    return render(request, "./index.html", {"form": form})

