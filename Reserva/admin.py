from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Mesa, Reserva, Empleado

admin.site.register(Mesa)
admin.site.register(Reserva)
admin.site.register(Empleado)
