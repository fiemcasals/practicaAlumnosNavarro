from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(
        required=False,
        label="Correo electrónico (opcional)",
        help_text="Opcional: ingresa tu correo electrónico."
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Tu nombre de usuario'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Tu email'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Elige una contraseña'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Repite tu contraseña'}),
        }

    error_messages = {
        'password_mismatch': _("Las contraseñas no coinciden."),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].help_text = _(
            "<ul class='text-muted small mb-0'>"
            "<li>Requerido: este campo no puede estar vacío.</li>"
            "<li>Debe tener 150 caracteres o menos.</li>"
            "<li>Solo puede contener letras, números y los símbolos @ . + - _</li>"
            "</ul>"
        )

        self.fields['password1'].help_text = _(
            "<ul class='text-muted small mb-0'>"
            "<li>Tu contraseña no debe ser muy similar a tu otra información personal.</li>"
            "<li>Debe contener al menos 8 caracteres.</li>"
            "<li>No puede ser una contraseña de uso común.</li>"
            "<li>No puede ser completamente numérica.</li>"
            "</ul>"
        )

        self.fields['password2'].help_text = _(
            "<ul class='text-muted small mb-0'>"
            "<li>Repite la misma contraseña para confirmarla.</li>"
            "</ul>"
        )

        for field_name, field in self.fields.items():
            css_class = 'form-control'
            if self.errors.get(field_name):
                css_class += ' is-invalid'
            field.widget.attrs.update({'class': css_class})

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError("El nombre de usuario debe tener al menos 3 caracteres.")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Ya existe un usuario con ese nombre.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un usuario con ese correo electrónico.")
        return email