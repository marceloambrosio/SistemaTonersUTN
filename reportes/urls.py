from django.urls import path
from . import views

urlpatterns = [
    path('toner_area/', views.TonerPorArea.as_view(), name="toner_area"),
]