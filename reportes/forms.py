from registro.models import Toner, Area, Impresora, Registro
from django.forms import ModelForm, TextInput, NumberInput, Select, DateInput
from reportes.models import TonerPorArea

class TonerPorAreaForm(ModelForm):
    class Meta:
        model = TonerPorArea
        fields = ['toner']
        widgets = {
            'toner': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
        }