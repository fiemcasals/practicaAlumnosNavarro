from django.db import models
from django.contrib.auth.models import User  # 👈 Importar modelo de usuario

class Nota(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notas')  # 👈 Nuevo campo
    title = models.CharField("Título", max_length=120, blank=True)
    body = models.TextField("Contenido")
    created_at = models.DateTimeField("Creada", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title or f"Nota #{self.pk}"