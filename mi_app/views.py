from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from datetime import datetime

def home(request):
    todas_las_tareas = Tarea.objects.all().order_by('-fecha_creacion')
    # Contamos cuántas tareas tienen completada=False
    pendientes = Tarea.objects.filter(completada=False).count() 
    
    contexto = {
        'nombre_usuario': 'Link',
        'fecha': datetime.now(),
        'lista_tareas': todas_las_tareas,
        'pendientes': pendientes # Lo pasamos al HTML
    }
    return render(request, 'mi_app/index.html', contexto)

def agregar_tarea(request):
    if request.method == "POST":
        nuevo_titulo = request.POST.get('titulo_tarea')
        if nuevo_titulo:
            Tarea.objects.create(titulo=nuevo_titulo)
    return redirect('home')

def completar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.completada = True
    tarea.save()
    return redirect('home')

def borrar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.delete()
    return redirect('home')