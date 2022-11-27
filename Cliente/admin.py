from django.contrib import admin

from .models import Cliente, Veiculo


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cpf', 'estado', 'cidade')


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('Cliente', 'veiculo', 'ano', 'placa', 'cor')
