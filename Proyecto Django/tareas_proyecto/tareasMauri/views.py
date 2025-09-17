from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note

def note_list_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tareasMauri:note_list_create")
    else:
        form = NoteForm()

    notes = Note.objects.all()
    return render(request, "tareasMauri/notes.html", {"form": form, "notes": notes})
