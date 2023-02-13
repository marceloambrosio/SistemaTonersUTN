from django.shortcuts import render
from django.views.generic import TemplateView
from registro.models import Registro
from reportes.filter import TonerPorAreaFilter

class InicioReportes(TemplateView):
    template_name = 'reportes.html'

def toner_area(request):
    toner_filter = TonerPorAreaFilter(request.GET, queryset=Registro.objects.all())
    context = {
        'form': toner_filter.form,
        'toner': toner_filter.qs,
        'cant' : len(toner_filter.qs)
    }

    return render(request, 'reportes/toner_area.html', context)