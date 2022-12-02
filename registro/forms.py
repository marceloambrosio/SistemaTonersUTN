from django import forms

class CrearNuevoToner(forms.Form):
    nombre = forms.CharField(label="Nombre de toner", max_length=50)