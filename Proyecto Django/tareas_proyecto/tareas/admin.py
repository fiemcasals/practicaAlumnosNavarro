from django.contrib import admin
from .models import Clase_tarea, Tarea

@admin.register(Clase_tarea)
class ClaseTareaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descripcion', 'completada', 'clase', 'fecha_creacion')
    list_filter = ('completada', 'clase')
    search_fields = ('titulo', 'descripcion')