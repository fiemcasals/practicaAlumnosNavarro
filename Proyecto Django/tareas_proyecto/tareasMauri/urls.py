from django.urls import path
from . import views

app_name = "treasMauri"

urlpatterns = [
    path("notas/", views.note_list_create, name="note_list_create"),
]
