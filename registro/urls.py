from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('areas/', views.mostrar_areas, name="areas"),
    path('impresoras/', views.mostrar_impresoras, name="impresoras"),
    path('toners/', views.mostrar_toners, name="toners"),
    path('registros/', views.mostrar_registros, name="registros"),
    path('new_area/', views.AreaCreateViews.as_view(), name="new_area"),
    path('new_impresora/', views.ImpresoraCreateViews.as_view(), name="new_impresora"),
    path('new_toner/', views.TonerCreateViews.as_view(), name="new_toner"),
    path('new_registro/', views.RegistroCreateViews.as_view(), name="new_registro"),
    path('edit_area/<int:pk>/', views.AreaUpdateViews.as_view(), name="edit_area"),
    path('edit_impresora/<int:pk>', views.ImpresoraUpdateViews.as_view(), name="edit_impresora"),
    path('edit_toner/<int:pk>', views.TonerUpdateViews.as_view(), name="edit_toner"),
    path('edit_registro/<int:pk>', views.RegistroUpdateViews.as_view(), name="edit_registro"),
    path('delete_area/<int:pk>/', views.AreaDeleteView.as_view(), name="delete_area"),
    path('delete_toner/<int:pk>/', views.TonerDeleteView.as_view(), name="delete_toner"),
    path('delete_impresora/<int:pk>/', views.ImpresoraDeleteView.as_view(), name="delete_impresora"),
    path('delete_registro/<int:pk>/', views.RegistroDeleteView.as_view(), name="delete_registro"),
]