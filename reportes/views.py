from django.shortcuts import render
from django.views.generic import TemplateView
from registro.models import Registro
from reportes.filter import TonerPorAreaFilter, TonerTotalesFilter
from django.forms import ModelForm, TextInput, NumberInput, Select, DateInput


class InicioReportes(TemplateView):
    template_name = 'reportes.html'


def toner_area(request):
    toner_filter = TonerPorAreaFilter(
        request.GET, queryset=Registro.objects.all())
    context = {
        'form': toner_filter.form,
        'toner': toner_filter.qs,
        'cant': len(toner_filter.qs)
    }

    return render(request, 'reportes/toner_area.html', context)


def toner_totales(request):
    toner_tic = TonerTotalesFilter(request.GET, queryset=Registro.objects.filter(impresora__area__nombre='TIC'))
    context = {
        'form': toner_tic.form,
        'tic' : len(toner_tic.qs)
    }

    return render(request, 'reportes/toner_totales.html', context)
