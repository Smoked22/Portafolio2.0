from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Cliente, Carta, Ingrediente, GuiaDesp, Suministro

admin.site.register(Cliente)
admin.site.register(Carta)
admin.site.register(Ingrediente)
admin.site.register(GuiaDesp)
admin.site.register(Suministro)
