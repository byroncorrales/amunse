from django.contrib import admin
from revistas.models import *
from django.contrib.contenttypes import generic

class RevistaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha','edicion']
    list_filter = ['fecha']
    search_fields = ['titulo']
    save_on_top = True
    date_hierarchy = 'fecha'
    list_per_page = 12

admin.site.register(Revista, RevistaAdmin)

