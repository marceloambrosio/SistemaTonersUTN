from django.contrib import admin
from .models import Toner, Area, Impresora, Registro
# Register your models here.

class AreaAdmin(admin.ModelAdmin):
    search_fields = ('nombre'),
    ordering = ['nombre']

class TonerAdmin(admin.ModelAdmin):
    search_fields = ('nombre'),
    ordering = ['nombre']

class ImpresoraAdmin(admin.ModelAdmin):
    ordering = ['marca']
    autocomplete_fields = ['area','toner']

class RegistroAdmin(admin.ModelAdmin):
    search_fields = ('impresora'),
    ordering = ['impresora']



admin.site.register(Toner, TonerAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Impresora, ImpresoraAdmin)
admin.site.register(Registro, RegistroAdmin)
