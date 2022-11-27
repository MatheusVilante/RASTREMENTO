from django.urls import path


from .views import TecnicoViewSet


urlpatterns = [
    path('tecnicos', TecnicoViewSet.as_view({'get': 'list'}), name='Tecnico')
]
