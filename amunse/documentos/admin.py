from django.contrib import admin
from documentos.models import *

class CategoriaDocumentoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']
    list_per_page = 12


class SubCategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria']
    list_filter = ['nombre']
    search_fields = ['nombre']
    list_per_page = 12
    
class ArchivoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha', 'subcategoria','categoria']
    list_filter = ['nombre', 'subcategoria']
    search_fields = ['nombre']
    list_per_page = 12

admin.site.register(CategoriaDocumento, CategoriaDocumentoAdmin)
admin.site.register(SubCategoriaDocumento, SubCategoriaAdmin)
admin.site.register(Archivo, ArchivoAdmin)

