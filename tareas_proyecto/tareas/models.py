from django.db import models
from django.contrib.auth.models import User  # 👈 Importar usuario

# Clase_tarea tiene un campo nombre.
# Tarea ahora tiene un campo clase que es un ForeignKey → una relación muchos-a-uno (varias tareas pueden estar dentro de una misma clase).
# on_delete=models.CASCADE significa que si eliminás una clase, también se borran sus tareas asociadas.
# related_name="tareas" permite acceder a todas las tareas de una clase con clase.tareas.all().

class Clase_tarea(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="tareas")  # 👈 Nuevo campo
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(default="Sin descripción")
    completada = models.BooleanField(default=False)
    clase = models.ForeignKey(Clase_tarea, on_delete=models.CASCADE, null=True, blank=True, related_name="tareas")
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # 👈 nuevo campo

    def __str__(self):
        return self.titulo        

        
