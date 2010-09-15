from django.contrib import admin
from noticias.models import *
from django.contrib.contenttypes import generic
from amunse.multimedia.models import Adjunto #importando el modelo de adjuntos genericos

class CategoriaNoticiaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']

class AdjuntoInline(generic.GenericStackedInline):
    model = Adjunto
    extra = 1
    max_num = 3

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha','categoria']
    list_filter = ['fecha', 'categoria']
    search_fields = ['titulo']
    inlines = [AdjuntoInline,]
    save_on_top = True
    date_hierarchy = 'fecha'
    
    class Media:
        js = ['../archivos/js/tiny_mce/tiny_mce.js',
              '../archivos/js/editores/textareas.js',]


admin.site.register(CategoriaNoticia, CategoriaNoticiaAdmin)
admin.site.register(Noticia, NoticiaAdmin)
