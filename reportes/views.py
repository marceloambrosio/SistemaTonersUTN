from django.shortcuts import render
from django.views.generic import TemplateView

class TonerPorArea(TemplateView):
    template_name = 'toner_area.html'