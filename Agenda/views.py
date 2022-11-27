from .models import Agenda
from .serializers import AgendaSerializer
from rest_framework import viewsets


class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
