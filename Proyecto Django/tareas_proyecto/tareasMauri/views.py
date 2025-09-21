from django.shortcuts import render, redirect, get_object_or_404
from .models import Nota
from .forms import NotaForm

# Vista para listar las notas
def lista_notas(request):
    notes = Nota.objects.order_by('-created_at')
    return render(request, "tareasMauri/notas.html", {
        "notes": notes,
        "active": "notas"
    })

# Vista para crear una nota
def crear_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tareasMauri:notas')
    else:
        form = NotaForm()
    return render(request, "tareasMauri/crear_notas.html", {
        "form": form,
        "active": "notas"
    })

# Vista para editar una nota
def editar_nota(request, id):
    nota = get_object_or_404(Nota, id=id)
    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect('tareasMauri:notas')
    else:
        form = NotaForm(instance=nota)
    return render(request, "tareasMauri/editar_nota.html", {
        "form": form,
        "nota": nota,
        "active": "notas"
    })

# Vista para eliminar una nota
def eliminar_nota(request, id):
    nota = get_object_or_404(Nota, id=id)
    nota.delete()
    return redirect('tareasMauri:notas')