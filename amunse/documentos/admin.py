from django.contrib import admin
from documentos.models import *

class CategoriaDocumentoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']
    prepopulated_fields = {'slug': ('nombre', )}

class SubCategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria']
    list_filter = ['nombre']
    search_fields = ['nombre']
    
class ArchivoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha', 'subcategoria']
    list_filter = ['nombre', 'subcategoria']
    search_fields = ['nombre']
    
    class Media:
        js = ['../archivos/js/tiny_mce/tiny_mce.js',
              '../archivos/js/editores/textareas.js']


admin.site.register(CategoriaDocumento, CategoriaDocumentoAdmin)
admin.site.register(SubCategoriaDocumento, SubCategoriaAdmin)
admin.site.register(Archivo, ArchivoAdmin)

