from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('areas/', views.mostrar_areas, name="areas"),
    path('impresoras/', views.mostrar_impresoras, name="impresoras"),
    path('toners/', views.mostrar_toners, name="toners"),
    path('new_area/', views.new_area, name="new_area"),
    path('new_impresora/', views.new_impresora, name="new_impresora"),
    path('new_toner/', views.new_toner, name="new_toner"),
    path('edit_area/<int:id>', views.edit_area, name="edit_area"),
    path('edit_impresora/<int:id>', views.edit_impresora, name="edit_impresora"),
    path('edit_toner/<int:id>', views.edit_toner, name="edit_toner"),
    path('edit_area/<int:id>/delete', views.delete_area, name="delete_area"),
]