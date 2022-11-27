from django.views.generic import View
from django.utils import timezone
from .models import *
from .render import Render
from .serializers import ServicoSerializer
from rest_framework import viewsets


class Pdf(View):
    def get(self, request):
        # teste = Seeder.seed(self)
        servicos = Servico.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'servicos': servicos,
            'request': request
        }
        return Render.render('pdf.html', params)


class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
