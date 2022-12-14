from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Area, Toner, Impresora
from .forms import CreateNewArea, CreateNewToner, CreateNewImpresora


# Create your views here.
def index(request):
    return render(request, 'index.html')

def mostrar_areas(request):
    areas = list(Area.objects.values())
    return render(request, 'area/listado_areas.html', {
        'areas': areas
    })
    #return JsonResponse(areas, safe=False)

def mostrar_toners(request):
    toners = list(Toner.objects.values())
    return render(request, 'toner/listado_toners.html', {
        'toners': toners
    })
    #return JsonResponse(toners, safe=False)

def mostrar_impresoras(request):
    impresoras = list(Impresora.objects.values())
    #return JsonResponse(impresoras, safe=False)
    return render(request, 'impresora/listado_impresoras.html', {
        'impresoras': impresoras
    })

""" def new_area(request):
    if request.method == 'GET':
        return render(request, 'area/new_area.html', {
            'form': CreateNewArea
        })
    else:
        Area.objects.create(
            nombre=request.POST['nombre'], responsable=request.POST['responsable'])
        return redirect('/areas') """
def new_area(request):
    if request.method == 'GET':
        return render(request, 'area/new_area.html', {
            'form': CreateNewArea
        })
    else:
        form = CreateNewArea(request.POST)
        form.save()
        return redirect('/areas')

def new_toner(request):
    if request.method == 'GET':
        return render(request, 'toner/new_toner.html', {
            'form': CreateNewToner
        })
    else:
        form = CreateNewToner(request.POST)
        form.save()
        return redirect('/toners')

def new_impresora(request):
    if request.method == 'GET':
        return render(request, 'impresora/new_impresora.html', {
            'form': CreateNewImpresora()
        })
    else:
        form = CreateNewImpresora(request.POST)
        form.save()
        return redirect('/impresoras')

def edit_area(request, id):
    if request.method == 'GET':
        area = get_object_or_404(Area, id=id)
        form = CreateNewArea(instance=area)
        return render(request, 'area/edit_area.html', {'area':area, 'form': form})
    else:
        area = get_object_or_404(Area, id=id)
        form = CreateNewArea(request.POST, instance=area)
        form.save()
        return redirect('/areas')

def selectToners(request):
    selectToners = Toner.objects.all()
    return render(request, 'new_impresora.html', {
        'selectToners': selectToners
    })