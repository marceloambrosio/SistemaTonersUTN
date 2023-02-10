from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView
from django_filters.rest_framework import DjangoFilterBackend
from registro.models import Registro
from django.core.paginator import Paginator
from django.http import Http404
from reportes.models import TonerPorArea
from reportes.filter import TonerPorAreaFilter
from reportes.forms import TonerPorAreaForm

class InicioReportes(TemplateView):
    template_name = 'reportes.html'

def toner_area(request):
    toner_filter = TonerPorAreaFilter(request.GET, queryset=Registro.objects.all())
    context = {
        'form': toner_filter.form,
        'toner': toner_filter.qs
    }

    return render(request, 'reportes/toner_area.html', context)