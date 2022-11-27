from django.urls import path


from .views import AgendaViewSet


urlpatterns = [
    path('agendamentos', AgendaViewSet.as_view({'get': 'list'}), name='agendamento')
]
