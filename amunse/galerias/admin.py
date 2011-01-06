from django.contrib import admin
from galerias.models import *
#from django.contrib.contenttypes import generic

class FotoAdmin(admin.ModelAdmin):
    list_display = ['titulo','image_img','galeria']
    search_fields = ['titulo']

class FotoInline(admin.StackedInline):
    model = ImagenAdjunta
    max_num = None
    extra = 1

class GaleriaAdmin(admin.ModelAdmin):
    list_display = ['titulo','tipo']
    search_fields = ['titulo']
    inlines = [FotoInline]



admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(ImagenAdjunta, FotoAdmin)

