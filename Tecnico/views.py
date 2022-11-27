from .models import Tecnico
from .serializers import TecnicoSerializer
from rest_framework import viewsets


class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer
