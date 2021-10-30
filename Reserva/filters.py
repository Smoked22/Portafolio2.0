import django_filters
from .models import Cliente

class ClienteFiltro(django_filters.FilterSet):
    class Meta:
        model = Cliente
        fields = ('__all__')
        exclude =('nombre','telefono','correo','dv')