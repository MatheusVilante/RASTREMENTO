from .models import Empresa
from .serializers import EmpresaSerializer
from rest_framework import viewsets


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
