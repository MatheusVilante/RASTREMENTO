from rest_framework import serializers

from .models import Pagamento


class PagamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pagamento
        fields = (
            'id',
            'funcionario',
            'Tecnico',
            'Empresa',
            'Cliente',
            'Veiculo',
            'forma_de_pag',
            'valor'
        )
