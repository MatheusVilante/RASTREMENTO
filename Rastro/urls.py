from django.contrib import admin
from django.urls import include

from rest_framework.routers import SimpleRouter
from Servico.views import Pdf, ServicoViewSet
from Tecnico.urls import *
from Agenda.urls import *
from Empresa.urls import *
from Cliente.urls import *
from Pagamento.urls import *

router = SimpleRouter()
router.register('tecnico', TecnicoViewSet)
router.register('agenda', AgendaViewSet)
router.register('empresa', EmpresaViewSet)
router.register('cliente', ClienteViewSet)
router.register('veiculo', VeiculoViewSet)
router.register('pagamento', PagamentoViewSet)
router.register('servico', ServicoViewSet
)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('render/pdf/', Pdf.as_view())
]
