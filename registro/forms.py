from django import forms
from .models import Toner, Area, Impresora
from django.forms import ModelForm

class CreateNewToner(ModelForm):
    class Meta:
        model = Toner
        fields = ['nombre']

class CreateNewArea(ModelForm):
    class Meta:
        model = Area
        fields = ['nombre', 'responsable']

class CreateNewImpresora(ModelForm):
    class Meta:
        model = Impresora
        fields = ['marca', 'modelo']


class SelectToner(forms.ModelForm):
    select_toner = forms.ModelChoiceField(queryset=Toner.objects.all())