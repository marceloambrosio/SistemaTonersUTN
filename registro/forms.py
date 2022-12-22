from django import forms
from .models import Toner, Area, Impresora, Registro
from django.forms import ModelForm, TextInput, NumberInput, Select, DateInput


class CreateNewToner(ModelForm):
    class Meta:
        model = Toner
        fields = ['nombre', 'stock']
        widgets = {
            'nombre': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ej: 253A'
                }
            ),
            'stock': NumberInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

class CreateNewArea(ModelForm):
    class Meta:
        model = Area
        fields = ['nombre', 'responsable']
        widgets = {
            'nombre': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'responsable': TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

class CreateNewImpresora(ModelForm):
    class Meta:
        model = Impresora
        fields = ['marca', 'modelo', 'toner', 'area']
        widgets = {
            'marca': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'modelo': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'toner': Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'area': Select(
                attrs={
                    'class': 'form-control',
                }
            )
        }

class CreateNewRegistro(ModelForm):
    class Meta:
        model = Registro
        fields = ['fecha', 'impresora', 'cantidad']
        widgets = {
            'fecha': DateInput(
                attrs={
                    'class': 'form-control',
                    'type' : 'date',
                }
            ),
            'impresora': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'cantidad': NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
