from rest_framework import serializers

from .models import Tecnico


class TecnicoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kargs = {
            'registro': {'write_only': True}
        }
        model = Tecnico
        fields = (
            'id',
            'nome',
            'estado',
            'cidade',
            'registro'
        )
