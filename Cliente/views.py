from .models import Cliente, Veiculo
from .serializers import ClienteSerializer, VeiculoSerializer
from rest_framework import viewsets


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class VeiculoViewSet(viewsets.ModelViewSet):
    queryset =Veiculo.objects.all()
    serializer_class = VeiculoSerializer

