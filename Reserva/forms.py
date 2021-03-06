from django import forms
from django.forms import fields
from .models import Reserva, Cliente
from django.contrib.auth import authenticate
from crispy_forms.helper import FormHelper
from django_select2 import forms as s2forms

class ReservaForm(forms.ModelForm):
    class Meta:
        model= Reserva
        fields=('__all__')
        helper = FormHelper()


class ClienteForm(forms.ModelForm):
    class Meta:
        model= Cliente
        fields=('__all__')
        helper = FormHelper()


