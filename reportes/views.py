from django.shortcuts import render
from django.views.generic import TemplateView

class InicioReportes(TemplateView):
    template_name = 'reportes.html'

class TonerPorArea(TemplateView):
    template_name = 'reportes/toner_area.html'