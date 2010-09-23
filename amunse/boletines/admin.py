from django.contrib import admin
from boletines.models import *
from django.contrib.contenttypes import generic

class BoletinAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha']
    list_filter = ['fecha']
    search_fields = ['titulo']
    save_on_top = True
    date_hierarchy = 'fecha'

admin.site.register(Boletin, BoletinAdmin)

