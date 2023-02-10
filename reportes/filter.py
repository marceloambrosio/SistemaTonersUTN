import django_filters
from registro.models import Registro

class TonerPorAreaFilter(django_filters.FilterSet):
    class Meta:
        model = Registro
        fields = {
            #'fecha', 'impresora', 'impresora__toner', 'impresora__area', 'cantidad'
            'impresora__toner': ['exact']
            }