from django.shortcuts import render
from django.views.generic import TemplateView
from registro.models import Registro
from reportes.filter import TonerPorAreaFilter, TonerTotalesFilter


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
    area_final = []
    area_sae = TonerTotalesFilter(request.GET, queryset=Registro.objects.all().filter(impresora__area__nombre='SAE'))
    area_tic = TonerTotalesFilter(request.GET, queryset=Registro.objects.all().filter(impresora__area__nombre='TIC'))
    area_final = [
        {'area':'SAE', 'cantidad':len(area_sae.qs)}, 
        {'area':'TIC', 'cantidad':len(area_tic.qs)}, 
        ]
    
    toner_final = []
    toner_105a = TonerTotalesFilter(request.GET, queryset=Registro.objects.all().filter(impresora__toner__nombre='105A'))
    toner_285u = TonerTotalesFilter(request.GET, queryset=Registro.objects.all().filter(impresora__toner__nombre='285U'))
    toner_final = [
        {'toner':'105A', 'cantidad':len(toner_105a.qs)},
        {'toner':'285U', 'cantidad':len(toner_285u.qs)},
    ]

    context = {
        'form': area_tic.form,
        'areas': area_final,
        'toners': toner_final,
    }

    return render(request, 'reportes/toner_totales.html', context)
