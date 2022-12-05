from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('areas/', views.mostrar_areas),
    path('impresoras/', views.mostrar_impresoras),
    path('toners/', views.mostrar_toners),
    path('new_area/', views.new_area, name="new_area"),
    path('new_impresora/', views.new_impresora, name="new_impresora"),
    path('new_toner/', views.new_toner, name="new_toner"),
]