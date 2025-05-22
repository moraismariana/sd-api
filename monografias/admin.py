from django.contrib import admin
from monografias.models import Monografia, Arquivo

class MonografiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo')
    list_display_links = ('id', 'titulo')

class ArquivoAdmin(admin.ModelAdmin):
    list_display = ('id', 'arquivo')
    list_display_links = ('id', 'arquivo')

admin.site.register(Monografia, MonografiaAdmin)
admin.site.register(Arquivo, ArquivoAdmin)