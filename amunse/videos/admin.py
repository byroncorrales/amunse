from django.contrib import admin
from videos.models import *
from django.contrib.contenttypes import generic

class VideoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha']
    list_filter = ['fecha']
    search_fields = ['titulo']
    save_on_top = True
    date_hierarchy = 'fecha'

admin.site.register(Video, VideoAdmin)

