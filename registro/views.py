from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from .models import Area, Toner, Impresora, Registro
from .forms import CreateNewArea, CreateNewToner, CreateNewImpresora, CreateNewRegistro
from django.core.paginator import Paginator
from django.views.generic import CreateView, UpdateView, DeleteView, View
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    return render(request, 'index.html')

def mostrar_areas(request):
    areas = Area.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(areas, 6)
        areas = paginator.page(page)
    except:
        raise Http404

    return render(request, 'area/listado_areas.html', {
        'entity': areas,
        'paginator': paginator
    })

def mostrar_toners(request):
    toners = Toner.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(toners, 6)
        toners = paginator.page(page)
    except:
        raise Http404

    return render(request, 'toner/listado_toners.html', {
        'entity': toners,
        'paginator': paginator
    })

def mostrar_impresoras(request):
    impresoras = Impresora.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(impresoras, 6)
        impresoras = paginator.page(page)
    except:
        raise Http404

    return render(request, 'impresora/listado_impresoras.html', {
        'entity': impresoras,
        'paginator': paginator
    })

class AreaCreateViews(SuccessMessageMixin, CreateView):
    model = Area
    form_class = CreateNewArea
    template_name = 'area/new_area.html'
    success_message = 'Se creo el area'
    success_url = reverse_lazy('areas')

class TonerCreateViews(SuccessMessageMixin, CreateView):
    model = Toner
    form_class = CreateNewToner
    template_name = 'toner/new_toner.html'
    success_message = 'Se creo el toner'
    success_url = reverse_lazy('toners')

class ImpresoraCreateViews(SuccessMessageMixin, CreateView):
    model = Impresora
    form_class = CreateNewImpresora
    template_name = 'impresora/new_impresora.html'
    success_message = 'Se creo la impresora'
    success_url = reverse_lazy('impresoras')

class RegistroCreateViews(SuccessMessageMixin, CreateView):
    model = Registro
    form_class = CreateNewRegistro
    template_name = 'registro/new_registro.html'
    success_message = 'Se creo el registro'
    success_url = reverse_lazy('registros')

    def form_valid(self, form):
        self.data = form.cleaned_data
        impresora = self.data['impresora']
        cantidad = self.data['cantidad']

        impresora = Impresora.objects.filter(id=impresora.id).first()
        print(impresora)
        print(impresora.toner)
        impresora.toner.stock = impresora.toner.stock - cantidad
        impresora.toner.save()
        form.save()
        return render(self.request, 'registros.html')

class AreaUpdateViews(SuccessMessageMixin, UpdateView):
    model = Area
    form_class = CreateNewArea
    template_name = 'area/edit_area.html'
    success_message = 'Se edito correctamente el area'
    success_url = reverse_lazy('areas')

class ImpresoraUpdateViews(SuccessMessageMixin, UpdateView):
    model = Impresora
    form_class = CreateNewImpresora
    template_name = 'impresora/edit_impresora.html'
    success_message = 'Se edito correctamente la impresora'
    success_url = reverse_lazy('impresoras')

class TonerUpdateViews(SuccessMessageMixin, UpdateView):
    model = Toner
    form_class = CreateNewToner
    template_name = 'toner/edit_toner.html'
    success_message = 'Se edito correctamente el toner'
    success_url = reverse_lazy('toners')

class AreaDeleteView(SuccessMessageMixin, DeleteView):
    model = Area
    success_url = reverse_lazy('areas')
    template_name = 'area/delete_area.html'
    success_message = 'Se elimino el area'

class TonerDeleteView(SuccessMessageMixin, DeleteView):
    model = Toner
    success_url = reverse_lazy('toners')
    template_name = 'toner/delete_toner.html'
    success_message = 'Se elimino el toner'

class ImpresoraDeleteView(SuccessMessageMixin, DeleteView):
    model = Impresora
    success_url = reverse_lazy('impresoras')
    template_name = 'impresora/delete_impresora.html'
    success_message = 'Se elimino la impresora'