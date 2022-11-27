from django.urls import path


from .views import PagamentoViewSet


urlpatterns = [
    path('empresas', PagamentoViewSet.as_view({'get': 'list'}), name='pagamento')
]
