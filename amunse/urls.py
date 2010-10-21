from django.conf.urls.defaults import *
import settings
from os import path as os_path
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^amunse/', include('amunse.foo.urls')),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^', include('paginas.urls')),
    (r'^', include('noticias.urls')),
    (r'^', include('boletines.urls')),
    (r'^', include('revistas.urls')),
    (r'^', include('municipios.urls')),
    (r'^', include('proyectos.urls')),
    (r'^', include('documentos.urls')),
    (r'^videos/', include('videos.urls')),
    (r'^eventos/', include('eventos.urls')),
    (r'^tags/(?P<id>\d+)$', 'paginas.views.tags'),
    (r'^busqueda/', include('haystack.urls')),
    (r'^$', 'paginas.views.inicio'),
    (r'^admin/filebrowser/', 'amunse.multimedia.views.subir_imagen'),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^tagging_autocomplete/', include('tagging_autocomplete.urls')),
)


if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^archivos/(.*)$', 'django.views.static.serve',
                             {'document_root': os_path.join(settings.MEDIA_ROOT)}),
                           )

