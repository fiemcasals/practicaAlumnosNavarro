from django import forms
from .models import Nota

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ["title", "body"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Título (opcional)"}),
            "body": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Escribí tu nota..."}),
        }
