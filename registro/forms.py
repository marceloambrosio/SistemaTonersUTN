from django import forms

class CreateNewToner(forms.Form):
    nombre = forms.CharField(label="Nombre de toner", max_length=50)

class CreateNewArea(forms.Form):
    nombre = forms.CharField(label="Nombre del area", max_length=50)
    responsable = forms.CharField(label="Nombre del responsable", max_length=50)