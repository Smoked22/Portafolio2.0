from django import forms
from django.forms import fields
from .models import Usuario
from django.contrib.auth import authenticate



# creating a form 

#class formLog(forms.ModelForm):
#    class Meta:
#        model = Usuario
#        fields = ['Nombre_de_usuario', 'password']