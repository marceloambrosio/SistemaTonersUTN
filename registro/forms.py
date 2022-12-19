from django import forms
from .models import Toner, Area, Impresora
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