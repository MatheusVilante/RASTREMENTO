from django.urls import path


from .views import ClienteViewSet, VeiculoViewSet


urlpatterns = [
    path('agendamentos', ClienteViewSet.as_view({'get': 'list'}), name='agendamento'),
    path('agendamentos', VeiculoViewSet.as_view({'get': 'list'}), name='agendamento')
]
