from django.contrib import admin
from galeria.models import Fotografia

class ListarFotos(admin.ModelAdmin):
    list_display = ('id','nome','legenda','categoria','publicada')
    list_display_links = ('id','nome')
    search_fields = ['nome']
    list_editable = ['publicada']
    list_filter = ['categoria']

admin.site.register(Fotografia,ListarFotos)
