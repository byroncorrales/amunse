from django.contrib import admin
from banners.models import *
#from django.contrib.contenttypes import generic

class BannerAdmin(admin.ModelAdmin):
    list_display = ['nombre','imagen']
    search_fields = ['nombre']


admin.site.register(Banner, BannerAdmin)
