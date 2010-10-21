from django.contrib import admin
from proyectos.models import *
from django.contrib.contenttypes import generic

class FinanciadorAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
    list_per_page = 12


class AreaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
    list_per_page = 12

class ProyectoAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['nombre', 'estado']
    list_filter = ['estado']
    list_per_page = 12
    search_fields = ['nombre']
    filter_horizontal = ('financiador','area')
    fieldsets = [
        (None, {'fields': ['nombre','monto','lugar']}),
        ('Periodo', {'fields': [('fecha_inicio','fecha_final')]}),
        (None, {'fields': ['estado','area','financiador','objetivos','resultados']}),
    ]
    
    class Media:
        js = ['../archivos/js/tiny_mce/tiny_mce.js',
              '../archivos/js/editores/textareas.js',]

admin.site.register(Financiador, FinanciadorAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
