from django.shortcuts import redirect, render

# Create your views here.

def home_finanzas(request):
    return render(request, './home_finanzas.html')