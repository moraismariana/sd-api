from django.urls import path, include
from rest_framework import routers

from monografias.views import MonografiaViewSet, ArquivoViewSet, UserDetailsView

router = routers.DefaultRouter()

router.register('monografias', MonografiaViewSet, basename='monografias')
router.register('arquivos', ArquivoViewSet, basename='arquivos')

urlpatterns = [
    path('', include(router.urls)),
    path('userdetails/', UserDetailsView.as_view(), name='userdetails'),
]
