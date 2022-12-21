from django import forms
from .models import Toner, Area, Impresora, Registro
from django.forms import ModelForm

class CreateNewToner(ModelForm):
    class Meta:
        model = Toner
        fields = ['nombre', 'stock']

class CreateNewArea(ModelForm):
    class Meta:
        model = Area
        fields = ['nombre', 'responsable']

class CreateNewImpresora(ModelForm):
    class Meta:
        model = Impresora
        fields = ['marca', 'modelo', 'toner', 'area']

class CreateNewRegistro(ModelForm):
    class Meta:
        model = Registro
        fields = ['fecha', 'impresora', 'cantidad']