from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Tarea
from .forms import TareaForm

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas/lista.html', {'tareas': tareas})

def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    return render(request, 'tareas/crear.html', {'form': form})   

# Busca la tarea por pk (id).
# Invierte (not) el valor de completada → si estaba en False, pasa a True, y viceversa.
# Guarda y redirige a la lista.
@require_POST
def toggle_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    tarea.completada = not tarea.completada
    tarea.save()
    return redirect('lista_tareas')

def editar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'tareas/editar.html', {'form': form, 'tarea': tarea})

@require_POST
def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    tarea.delete()
    return redirect('lista_tareas')    