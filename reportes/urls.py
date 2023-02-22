from django.urls import path
from reportes import views

urlpatterns = [
    path('', views.InicioReportes.as_view(), name="inicio_reportes"),
    path('export/', views.export_pdf, name="export_pdf"),
    path('toner_area/', views.toner_area, name="toner_area"),
    path('toner_totales/', views.toner_totales, name="toner_totales"),
]