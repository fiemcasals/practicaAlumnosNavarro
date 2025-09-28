from django.contrib import admin
from .models import Nota

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'created_at')
    search_fields = ('title', 'body')
    list_filter = ('created_at',)