from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Toner, Impresora
from .forms import CrearNuevoToner


# Create your views here.
def index(request):
    return render(request, index.html)

def mostrar_area(request, id):
    print(id)
    return HttpResponse("Hola %s" % id)

def mostrar_toner(request):
    toners = list(Toner.objects.values())
    return JsonResponse(toners, safe=False)

def mostrar_impresora(request):
    toners = list(Impresora.objects.values())
    return JsonResponse(toners, safe=False)

def nuevo_toner(request):
    return render(request, 'nuevo_toner.html', {
        'form': CrearNuevoToner
    })