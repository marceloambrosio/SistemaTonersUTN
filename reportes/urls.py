from django.urls import path
from . import views

urlpatterns = [
    path('', views.InicioReportes.as_view(), name="inicio_reportes"),
    path('toner_area/', views.TonerPorArea.as_view(), name="toner_area"),
]