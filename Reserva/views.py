from django.shortcuts import redirect, render, redirect, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    return render(request, './home_reserva.html')


@login_required
def reservas(request):
    return render(request, './reservas.html')    
