from django.db import models
import os

# Função para definir o diretório de upload dinamicamente
def monografia_diretorio_upload(instance, filename):
    return f'monografias/{instance.monografia.id}/{filename}'

class Monografia(models.Model):
    titulo = models.CharField(max_length=1000, blank=False, null=False)
    autor = models.CharField(max_length=500, blank=False, null=False)
    orientador = models.CharField(max_length=500, blank=False, null=False)
    coorientador = models.CharField(max_length=500, blank=True, null=True)
    resumo = models.TextField()
    abstract = models.TextField()
    palavras_chave = models.TextField()
    data_defesa = models.DateField()
    def __str__(self):
        return self.titulo

class Arquivo(models.Model):
    monografia = models.ForeignKey(
        Monografia,
        related_name='arquivos',
        on_delete=models.CASCADE
    )
    nome_arquivo = models.CharField(max_length=500, blank=False, null=False, default="nome-do-arquivo.pdf")
    arquivo = models.FileField(upload_to=monografia_diretorio_upload)

    def __str__(self):
        return f"{os.path.basename(self.arquivo.name)} ({self.monografia.titulo})"
