from django.shortcuts import render, redirect, get_object_or_404 
from django.views.decorators.http import require_POST
from .models import Tarea
from .forms import TareaForm
from tareasMauri.models import Nota   # 👉 importar el modelo Nota


def index(request):
    total_tareas = Tarea.objects.count()
    total_notas = Nota.objects.count()  # 👉 contar las notas
    return render(
        request,
        "index.html",
        {
            "total_tareas": total_tareas,
            "total_notas": total_notas,   # 👉 pasarlo al template
        },
    )


def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas/lista.html', {
        'tareas': tareas,
        'active': 'tareas'
    })


def dashboard(request):
    tareas_count = Tarea.objects.count()
    notas_count = Nota.objects.count()  # 👉 usar directamente Nota

    return render(request, 'tareas/dashboard.html', {
        'tareas_count': tareas_count,
        'notas_count': notas_count,
        'active': 'dashboard'
    })    


def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tareas:lista_tareas')  # 👉 usar namespace si lo tenés definido
    else:
        form = TareaForm()
    return render(request, 'tareas/crear.html', {'form': form})   


@require_POST
def toggle_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    tarea.completada = not tarea.completada
    tarea.save()
    return redirect('tareas:lista_tareas')


def editar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('tareas:lista_tareas')
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'tareas/editar.html', {
        'form': form,
        'tarea': tarea
    })


@require_POST
def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    tarea.delete()
    return redirect('tareas:lista_tareas')