from django.contrib import admin

from .models import Tecnico


@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estado', 'cidade', 'registro', 'disponivel', 'contratacao')
