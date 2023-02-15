from django.shortcuts import render
from django.views.generic import TemplateView
from registro.models import Registro, Area, Toner
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
    areas = []
    toners = []
    areas = Area.objects.all().order_by('nombre')
    toners = Toner.objects.all().order_by('nombre')
    area_final = []
    toner_final = []

    for a in areas:
        area_filter = TonerTotalesFilter(request.GET, queryset=Registro.objects.all().filter(impresora__area=a))
        area_final.append({'area':a.nombre, 'cantidad':len(area_filter.qs)})     
    
    for t in toners:
        toner_filter = TonerTotalesFilter(request.GET, queryset=Registro.objects.all().filter(impresora__toner=t))
        toner_final.append({'toner':t.nombre, 'cantidad':len(toner_filter.qs)})     

    context = {
        'form': area_filter.form,
        'areas': area_final,
        'toners': toner_final,
    }       
    
    return render(request, 'reportes/toner_totales.html', context)