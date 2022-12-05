from django.contrib import admin
from .models import Toner, Area, Impresora
# Register your models here.

class TonerAdmin(admin.ModelAdmin):
    search_fields = ('nombre')
    ordering = ['nombre']

class ImpresoraAdmin(admin.ModelAdmin):
    ordering = ['nombre']
    autocomplete_fields = ['toner']
