from django.shortcuts import render
from django.views.generic import TemplateView
from django_filters.rest_framework import DjangoFilterBackend
from registro.models import Registro
from django.core.paginator import Paginator
from django.http import Http404
import django_filters

class InicioReportes(TemplateView):
    template_name = 'reportes.html'

""" class TonerPorArea(TemplateView):
    template_name = 'reportes/toner_area.html'
    name = django_filters.CharFilter(lookup_expr='iexact')
    area = django_filters.CharFilter

    class Meta:
        model = Registro
        fields = ['fecha', 'area'] """

def toner_area(request):
    toners = Registro.objects.all().filter(impresora__toner__nombre="285U").order_by('fecha')
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(toners, 6)
        toners = paginator.page(page)
    except:
        raise Http404

    return render(request, 'reportes/toner_area.html', {
        'entity': toners,
        'paginator': paginator
    })