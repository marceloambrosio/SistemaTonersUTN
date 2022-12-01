from django.urls import path
from . import views

urlpatterns = [
    path('area/<int:id>', views.mostrar_area),
    path('impresora/<int:id>', views.mostrar_area),
    path('toner/<int:id>', views.mostrar_area),
]