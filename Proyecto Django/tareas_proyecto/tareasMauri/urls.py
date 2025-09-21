from django.urls import path
from . import views

app_name = "tareasMauri"

urlpatterns = [
    path("notas/", views.lista_notas, name="notas"),
    path("crear_notas/", views.crear_nota, name="crear_notas"),
    path("editar_nota/<int:id>/", views.editar_nota, name="editar_nota"),
    path("eliminar_nota/<int:id>/", views.eliminar_nota, name="eliminar_nota"),
]