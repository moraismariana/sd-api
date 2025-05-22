from django.db import models
import os
from django.db.models.signals import pre_delete
from django.dispatch import receiver

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

    def delete(self, *args, **kwargs):
        caminho_do_arquivo_para_log = None
        nome_do_arquivo_original_para_log = None

        if self.arquivo and self.arquivo.name:
            nome_do_arquivo_original_para_log = self.arquivo.name
            try:
                caminho_do_arquivo_para_log = self.arquivo.path
            except ValueError:
                pass

        if self.arquivo:
            if caminho_do_arquivo_para_log and os.path.isfile(caminho_do_arquivo_para_log):
                try:
                    self.arquivo.delete(save=False)
                    print(f"Arquivo {caminho_do_arquivo_para_log} deletado (via método delete).")
                except Exception as e:
                    print(f"Erro ao deletar o arquivo físico {caminho_do_arquivo_para_log}: {e}")
            elif nome_do_arquivo_original_para_log:
                print(f"Arquivo {nome_do_arquivo_original_para_log} (caminho: {caminho_do_arquivo_para_log or 'não resolvido/inválido'}) não encontrado no sistema de arquivos. Registro será deletado.")

        super().delete(*args, **kwargs)
    def __str__(self):
        return f"{os.path.basename(self.arquivo.name)} ({self.monografia.titulo})"