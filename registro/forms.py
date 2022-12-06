from django import forms
from .models import Toner

class CreateNewToner(forms.Form):
    nombre = forms.CharField(label="Nombre de toner", max_length=50)

class CreateNewArea(forms.Form):
    nombre = forms.CharField(label="Nombre del area", max_length=50)
    responsable = forms.CharField(label="Nombre del responsable", max_length=50)

class CreateNewImpresora(forms.Form):
    marca = forms.CharField(label="Marca", max_length=50)
    modelo = forms.CharField(label="Modelo", max_length=50)
    #toner = forms.Select()

class SelectToner(forms.ModelForm):
    select_toner = forms.ModelChoiceField(queryset=Toner.objects.all())