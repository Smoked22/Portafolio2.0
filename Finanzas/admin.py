from django.contrib import admin
from .models import Boleta, Orden, Mesa
# Register your models here.

admin.site.register(Boleta)
admin.site.register(Orden)
admin.site.register(Mesa)