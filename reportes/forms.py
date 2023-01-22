from registro.models import Toner, Area, Impresora, Registro
from django.forms import ModelForm, TextInput, NumberInput, Select, DateInput

class TonerArea(ModelForm):
    class Meta:
        model = Registro
        fields = ['fecha¨_desde', 'fecha_hasta', 'area', 'impresora']
        widgets = {
            'fecha_desde': DateInput(
                attrs={
                    'class': 'form-control',
                    'type' : 'date',
                }
            ),
            'fecha_hasta': DateInput(
                attrs={
                    'class': 'form-control',
                    'type' : 'date',
                }
            ),
            'area': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'impresora': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
        }