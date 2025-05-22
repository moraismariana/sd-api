from rest_framework import viewsets

from monografias.models import Monografia, Arquivo
from monografias.serializers import MonografiaSerializer, ArquivoSerializer

class MonografiaViewSet(viewsets.ModelViewSet):
    queryset = Monografia.objects.all()
    serializer_class = MonografiaSerializer

class ArquivoViewSet(viewsets.ModelViewSet):
    queryset = Arquivo.objects.all()
    serializer_class = ArquivoSerializer
