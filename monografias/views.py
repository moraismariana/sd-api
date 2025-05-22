from rest_framework import viewsets, filters as drf_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from monografias.models import Monografia, Arquivo
from monografias.serializers import MonografiaSerializer, ArquivoSerializer
from monografias.filters import MonografiaFilter

class MonografiaViewSet(viewsets.ModelViewSet):
    queryset = Monografia.objects.all().order_by('-data_defesa', '-id')
    serializer_class = MonografiaSerializer
    filter_backends = [
        drf_filters.SearchFilter,
        DjangoFilterBackend,
        drf_filters.OrderingFilter
    ]

    search_fields = [
        'titulo',
        'autor',
        'orientador',
        'coorientador',
        'resumo',
        'abstract',
        'palavras_chave'
    ]

    filterset_class = MonografiaFilter

    ordering_fields = ['titulo', 'autor', 'orientador', 'data_defesa']
    ordering = ['-data_defesa']

class ArquivoViewSet(viewsets.ModelViewSet):
    queryset = Arquivo.objects.all()
    serializer_class = ArquivoSerializer

class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        groups = [group.name for group in user.groups.all()]
        return Response({
            'username': user.username,
            'groups': groups,
        })