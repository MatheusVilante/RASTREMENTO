from rest_framework import serializers

from .models import Empresa


class EmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kargs = {
            'cnpj': {'write_only': True}
        }
        model = Empresa
        fields = (
            'id',
            'nome',
            'estado',
            'cidade',
            'cnpj'
        )
