from django.contrib import admin

from .models import Pagamento


@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = (
            'id',
            'funcionario',
            'Tecnico',
            'Empresa',
            'Cliente',
            'Veiculo',
            'forma_de_pag',
            'valor'
        )
    