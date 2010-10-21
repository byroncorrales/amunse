from django.contrib import admin
from municipios.models import *
#from django.contrib.contenttypes import generic
#from amunse.multimedia.models import Adjunto #importando el modelo de adjuntos genericos


class MunicipioAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
    list_per_page = 12
    save_on_top = True

    class Media:
        js = ['../archivos/js/tiny_mce/tiny_mce.js',
              '../archivos/js/editores/textareas.js',]

admin.site.register(Municipio, MunicipioAdmin)

