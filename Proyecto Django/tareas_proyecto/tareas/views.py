from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Tarea
from .forms import TareaForm
from tareasMauri.models import Nota


# Página de inicio (estadísticas globales del usuario logueado)
@login_required
def index(request):
    total_tareas = Tarea.objects.filter(user=request.user).count()
    total_notas = Nota.objects.filter(user=request.user).count()
    return render(
        request,
        "index.html",
        {
            "total_tareas": total_tareas,
            "total_notas": total_notas,
        },
    )


# Lista de tareas del usuario logueado con buscador
from django.db.models import Q

@login_required
def lista_tareas(request):
    busqueda = request.GET.get('buscar', '')

    # Filtra solo las tareas del usuario logueado
    tareas = Tarea.objects.filter(user=request.user)



    # Si hay búsqueda, filtra por título o descripción
    if busqueda:
        tareas = tareas.filter(
            Q(titulo__icontains=busqueda) |
            Q(descripcion__icontains=busqueda)
        )

    tareas = tareas.order_by('-fecha_creacion')  # Orden por fecha

    return render(request, 'tareas/lista.html', {
        'tareas': tareas,
        'busqueda': busqueda
    })



# Dashboard (resumen del usuario actual)
@login_required
def dashboard(request):
    tareas_count = Tarea.objects.filter(user=request.user).count()
    notas_count = Nota.objects.filter(user=request.user).count()

    return render(request, 'tareas/dashboard.html', {
        'tareas_count': tareas_count,
        'notas_count': notas_count,
        'active': 'dashboard'
    })


# Crear tarea asociada al usuario actual
@login_required
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.user = request.user  # 👈 Asociar al usuario actual
            tarea.save()
            return redirect('tareas:lista_tareas')
    else:
        form = TareaForm()

    return render(request, 'tareas/crear.html', {'form': form})


# Alternar el estado de completada (solo si pertenece al usuario)
@login_required
@require_POST
def toggle_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk, user=request.user)
    tarea.completada = not tarea.completada
    tarea.save()
    return redirect('tareas:lista_tareas')


# Editar tarea (solo del usuario)
@login_required
def editar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk, user=request.user)
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


# Eliminar tarea (solo del usuario actual)
@login_required
@require_POST
def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk, user=request.user)
    tarea.delete()
    return redirect('tareas:lista_tareas')