from django.contrib import admin
from documentos.models import *

class CategoriaDocumentoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']


class SubCategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria']
    list_filter = ['nombre']
    search_fields = ['nombre']
    
class ArchivoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha', 'subcategoria','categoria']
    list_filter = ['nombre', 'subcategoria']
    search_fields = ['nombre']
    
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
              



admin.site.register(CategoriaDocumento, CategoriaDocumentoAdmin)
admin.site.register(SubCategoriaDocumento, SubCategoriaAdmin)
admin.site.register(Archivo, ArchivoAdmin)

