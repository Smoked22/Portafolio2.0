from django import forms
from django.forms import fields
from .models import Ingrediente
from django.contrib.auth import authenticate
from crispy_forms.helper import FormHelper

class IngredienteForm(forms.ModelForm):

    class Meta:
        model= Ingrediente
        fields=('id_ingrediente','nom_ingrediente','desc_ingrediente','stock','unidad_de_medida','fec_caduc')
        helper = FormHelper()



# creating a form 

#class formLog(forms.ModelForm):
#    class Meta:
#        model = Usuario
#        fields = ['Nombre_de_usuario', 'password']