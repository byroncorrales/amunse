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
    
#    class Media:
#        js = ['../archivos/js/autocomplete/jquery.autocomplete.js',
#              '../archivos/js/autocomplete/lib/jquery.bgiframe.min.js',
#              '../archivos/js/autocomplete/lib/jquery.bgiframe.min.js',
#              '../archivos/js/autocomplete/lib/jquery.ajaxQueue.js',
#              '../archivos/js/autocomplete/lib/thickbox-compressed.js',
#              '../archivos/js/autocomplete/lib/jquery.js']
#              '../archivos/js/autocomplete/tiny_mce.js',
              
#        css = ['../archivos/css/jquery.autocomplete.css',
#                '../archivos/css/thickbox.css',]
              



admin.site.register(CategoriaNoticia, CategoriaNoticiaAdmin)
admin.site.register(Noticia, NoticiaAdmin)
