from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

# Create your views here.

@login_required
def home_finanzas(request):
    return render(request, './home_finanzas.html')

@login_required
def boletas(request):
    return render(request, './registro_boletas.html')