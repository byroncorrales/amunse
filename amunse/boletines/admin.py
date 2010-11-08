from boletines.models import *
from django.contrib import admin
from django.contrib.contenttypes import generic
#from amunse.boletines.actions import *
#admin.site.disable_action('delete_selected')


class BoletinAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha']
    list_filter = ['fecha']
    search_fields = ['titulo']
    save_on_top = False
    date_hierarchy = 'fecha'
    list_per_page = 12
    #actions = ['delete_selected']

    #def delete_selected(self, request, queryset):
    #    print queryset
    #    for obj in queryset:
    #        obj.delete()
                     
    #delete_selected.short_description = "Eliminar los boletines seleccionados"

admin.site.register(Boletin, BoletinAdmin)
