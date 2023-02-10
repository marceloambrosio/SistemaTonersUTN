import django_filters
from registro.models import Registro
from django.forms import ModelForm, TextInput, NumberInput, Select, DateInput

class TonerPorAreaFilter(django_filters.FilterSet):
    fecha = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Registro
        fields = {
            #'fecha', 'impresora', 'impresora__toner', 'impresora__area', 'cantidad'
            'impresora__toner': ['exact']
            }
        widgets = {
            'impresora__toner': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'fecha': DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            )
        }