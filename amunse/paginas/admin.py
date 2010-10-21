from django.contrib import admin
from paginas.models import *
from django.contrib.contenttypes import generic
from amunse.multimedia.models import Adjunto #importando el modelo de adjuntos genericos

class AdjuntoInline(generic.GenericStackedInline):
    model = Adjunto
    extra = 1
    max_num = 3

class PaginaAdmin(admin.ModelAdmin):
    list_display = ['titulo','fecha']
    list_filter = ['fecha']
    search_fields = ['titulo']
#    inlines = [AdjuntoInline,]
    save_on_top = True
    date_hierarchy = 'fecha'
    list_per_page = 12

    class Media:
        js = ['../archivos/js/tiny_mce/tiny_mce.js',
              '../archivos/js/editores/textareas.js',]

class MenuPrimarioAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'orden']
    search_fields = ['titulo']

class MenuSecundarioAdmin(admin.ModelAdmin):
    list_display = ['titulo','menuprimario', 'orden','pagina','url']
    search_fields = ['titulo']
    list_filter = ['menuprimario']
    list_per_page = 12

admin.site.register(Pagina, PaginaAdmin)
admin.site.register(MenuPrimario, MenuPrimarioAdmin)
admin.site.register(MenuSecundario, MenuSecundarioAdmin)
