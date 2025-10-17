from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    # Página de inicio de sesión
    path('login/', views.login_usuario, name='login'),
    # Cierre de sesión (por POST preferiblemente, pero aceptamos GET para mayor compatibilidad)
    path('logout/', views.logout_usuario, name='logout'),
    path('registro/', views.registro_usuario, name='registro'),  # 👈 nueva ruta
]