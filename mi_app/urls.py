from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agregar/', views.agregar_tarea, name='agregar'),
    path('completar/<int:tarea_id>/', views.completar_tarea, name='completar'),
    path('borrar/<int:tarea_id>/', views.borrar_tarea, name='borrar'),
]