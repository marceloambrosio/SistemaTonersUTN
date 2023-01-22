from django.shortcuts import render
from django.views.generic import TemplateView
from django_filters.rest_framework import DjangoFilterBackend
from registro.models import Registro
import django_filters

class InicioReportes(TemplateView):
    template_name = 'reportes.html'

class TonerPorArea(TemplateView):
    template_name = 'reportes/toner_area.html'
    name = django_filters.CharFilter(lookup_expr='iexact')
    area = django_filters.CharFilter

    class Meta:
        model = Registro
        fields = ['fecha', 'area']