from rest_framework import serializers

from .models import Cliente, Veiculo


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kargs = {
            'cpf': {'write_only': True}
        }
        model = Cliente
        fields = (
            'id',
            'nome',
            'sobrenome',
            'cpf',
            'estado',
            'cidade',
            'rua',
            'numero',
            'complemento',
            'bairro'
        )


class VeiculoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Veiculo
        fields = (
            'id',
            'Cliente',
            'veiculo',
            'ano',
            'placa',
            'renavam',
            'chassi',
            'cor'
        )
