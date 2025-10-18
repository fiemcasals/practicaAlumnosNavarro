# tareas/forms.py
from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'completada', 'clase']  # 👈 agregamos 'clase'
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'completada': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'clase': forms.Select(attrs={'class': 'form-select'}),  # 👈 dropdown bonito con Bootstrap
        }