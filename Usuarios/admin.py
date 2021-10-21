from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Cliente, Menu

admin.site.register(Cliente)
admin.site.register(Menu)