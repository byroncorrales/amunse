from django.conf.urls.defaults import *
from django.conf import settings
from models import Archivo, CategoriaDocumento, SubCategoriaDocumento 

urlpatterns = patterns('documentos.views',
    (r'^documentos/$', 'categoria_lista'),
    (r'^documentos/(?P<slug_cat>[-\w]+)/$', 'subcategoria_lista'),
    (r'^documentos/(?P<slug_cat>[-\w]+)/(?P<slug_subcat>[-\w]+)/$', 'archivo_lista'),
    (r'^documentos/(?P<slug_cat>[-\w]+)/(?P<slug_subcat>[-\w]+)/(?P<archivo_slug>[-\w]+)$', 'archivo_detalle'),
)
