from re import search
from django.contrib import admin
from registros.models import Objeto, Localizacao #ObjetoLocalizacao


class Objetos (admin.ModelAdmin):
    list_display = ('numeroDeOrdem', 'estadoNacao', 'nome', 'classe', 'tipo', 'causa', 'posicao', 'bandeira', 'localizacao')
    list_display_links = ('numeroDeOrdem', 'estadoNacao', 'nome', 'classe', 'tipo', 'causa', 'posicao', 'bandeira', 'localizacao')
    search_fields = ('numeroDeOrdem',)
    list_per_page = 200

admin.site.register (Objeto, Objetos) 

class Localizacoes (admin.ModelAdmin):
    list_display = ('numeroDeOrdem', 'pnt')
    list_display_links = ('numeroDeOrdem', 'pnt')
    search_fields = ('numeroDeOrdem',)
    list_per_page = 200

admin.site.register (Localizacao, Localizacoes) 

"""
class ObjetosLocalizacoes (admin.ModelAdmin):
    list_display = ( 'numeroDeOrdem', 'estadoNacao')
    list_display_links = ( 'estadoNacao',)
    search_fields = ('numeroDeOrdem', ' estadoNacao')
    list_per_page = 200

admin.site.register (ObjetoLocalizacao, ObjetosLocalizacoes) 

"""