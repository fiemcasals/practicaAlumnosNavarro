from django.urls import path
from . import views

app_name = 'tareas'   # 👈 importante!

urlpatterns = [
    path('', views.dashboard, name='dashboard'),              # dashboard principal
    path('tareas/', views.lista_tareas, name='lista_tareas'), # lista de tareas
    path('tareas/crear/', views.crear_tarea, name='crear_tarea'),

    # Para cambiar el estado, editar y eliminar
    path('tarea/<int:pk>/toggle/', views.toggle_tarea, name='toggle_tarea'),
    path('tarea/<int:pk>/editar/', views.editar_tarea, name='editar_tarea'),
    path('tarea/<int:pk>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),
]
