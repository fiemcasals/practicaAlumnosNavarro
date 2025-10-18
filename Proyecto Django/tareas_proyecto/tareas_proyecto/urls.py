"""
URL configuration for tareas_proyecto project.
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Apps del proyecto
    path('', include(('tareas.urls', 'tareas'), namespace='tareas')),
    path('mauri/', include(('tareasMauri.urls', 'tareasMauri'), namespace='tareasMauri')),
    path('usuarios/', include('usuarios.urls')),

    # Login clásico de Django
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='tareas:dashboard'), name='logout'),

    # Login con Google (OAuth2)
    path('oauth/', include('social_django.urls', namespace='social')),
]