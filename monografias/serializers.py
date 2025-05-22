from rest_framework import serializers
from monografias.models import Monografia, Arquivo

class ArquivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arquivo
        fields = '__all__'

class MonografiaSerializer(serializers.ModelSerializer):
    arquivos = ArquivoSerializer(many=True, read_only=True)

    class Meta:
        model = Monografia
        fields = [
            'id',
            'titulo',
            'autor',
            'orientador',
            'coorientador',
            'resumo',
            'abstract',
            'palavras_chave',
            'data_defesa',
            'arquivos'
        ]