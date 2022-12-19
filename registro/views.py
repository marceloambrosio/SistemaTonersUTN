from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from .models import Area, Toner, Impresora
from .forms import CreateNewArea, CreateNewToner, CreateNewImpresora
from django.core.paginator import Paginator


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

def edit_impresora(request, id):
    if request.method == 'GET':
        impresora = get_object_or_404(Impresora, id=id)
        form = CreateNewImpresora(instance=impresora)
        return render(request, 'impresora/edit_impresora.html', {'impresora':impresora, 'form': form})
    else:
        impresora = get_object_or_404(Impresora, id=id)
        form = CreateNewImpresora(request.POST, instance=impresora)
        form.save()
        return redirect('/impresoras')

def edit_toner(request, id):
    if request.method == 'GET':
        toner = get_object_or_404(Toner, id=id)
        form = CreateNewToner(instance=toner)
        return render(request, 'toner/edit_toner.html', {'toner':toner, 'form': form})
    else:
        toner = get_object_or_404(Toner, id=id)
        form = CreateNewToner(request.POST, instance=toner)
        form.save()
        return redirect('/toners')

def delete_area(request, id):
    area = get_object_or_404(Area, id=id)
    if request.method == 'GET':
        return render(request, 'area/delete_area.html', {'area':area})
    else:
        area.delete()
        return redirect('/areas')

def delete_toner(request, id):
    toner = get_object_or_404(Toner, id=id)
    if request.method == 'GET':
        return render(request, 'toner/delete_toner.html', {'toner':toner})
    else:
        toner.delete()
        return redirect('/toners')

def delete_impresora(request, id):
    impresora = get_object_or_404(Impresora, id=id)
    if request.method == 'GET':
        return render(request, 'impresora/delete_impresora.html', {'impresora':impresora})
    else:
        impresora.delete()
        return redirect('/impresoras')

def selectToners(request):
    selectToners = Toner.objects.all()
    return render(request, 'new_impresora.html', {
        'selectToners': selectToners
    })