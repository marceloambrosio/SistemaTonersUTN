from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mostrar_area(request, id):
    print(id)
    return HttpResponse("Hola %s" % id)