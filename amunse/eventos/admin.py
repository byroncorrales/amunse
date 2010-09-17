from django.contrib import admin
from eventos.models import *
from django.contrib.contenttypes import generic
from amunse.multimedia.models import Adjunto #importando el modelo de adjuntos genericos

class AdjuntoInline(generic.GenericStackedInline):
    model = Adjunto
    extra = 1
    max_num = 3

class EventoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_inicio','fecha_final']
    list_filter = ['fecha_inicio']
    search_fields = ['titulo']
    inlines = [AdjuntoInline,]
    save_on_top = True
    date_hierarchy = 'fecha_inicio'
    
    class Media:
        js = ['../archivos/js/tiny_mce/tiny_mce.js',
              '../archivos/js/editores/textareas.js',]


admin.site.register(Evento, EventoAdmin)

