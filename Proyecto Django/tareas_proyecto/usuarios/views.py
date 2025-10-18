from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .forms import RegistroUsuarioForm


@require_http_methods(["GET", "POST"])
def login_usuario(request):
    """Vista para iniciar sesión."""
    if request.user.is_authenticated:
        return redirect('tareas:dashboard')

    next_url = request.GET.get('next') or request.POST.get('next') or None

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(next_url or 'tareas:dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'usuarios/login.html', {'next': next_url})


@require_http_methods(["GET", "POST"])
def logout_usuario(request):
    """Cierra la sesión del usuario."""
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "Has cerrado sesión correctamente.")
    return redirect('usuarios:login')


@require_http_methods(["GET", "POST"])
def registro_usuario(request):
    """Vista para registrar nuevos usuarios con validación completa."""
    if request.user.is_authenticated:
        messages.info(request, "Ya has iniciado sesión.")
        return redirect('tareas:dashboard')

    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cuenta creada correctamente. ¡Ahora puedes iniciar sesión!")
            return redirect('usuarios:login')
        else:
            messages.error(request, "Por favor corrige los errores indicados debajo de cada campo.")
    else:
        form = RegistroUsuarioForm()

    return render(request, 'usuarios/registro.html', {'form': form})