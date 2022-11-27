from django.urls import path


from .views import EmpresaViewSet


urlpatterns = [
    path('empresas', EmpresaViewSet.as_view({'get': 'list'}), name='Empresa')
]
