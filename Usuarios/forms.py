from django import forms
from django.forms import fields
from .models import Ingrediente
from django.contrib.auth import authenticate

class IngredienteForm(forms.ModelForm):

    class Meta:
        model= Ingrediente
        fields='__all__'
        


# creating a form 

#class formLog(forms.ModelForm):
#    class Meta:
#        model = Usuario
#        fields = ['Nombre_de_usuario', 'password']