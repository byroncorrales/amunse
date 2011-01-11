from django.conf.urls.defaults import *
from django.conf import settings
from models import Galeria, ImagenAdjunta 

urlpatterns = patterns('galerias.views',
    (r'^galerias/tipo/(?P<tipo_gal>[-\w]+)/$', 'lista'),
    (r'^galerias/tipo/(?P<tipo_gal>[-\w]+)/(?P<slug>[-\w]+)$', 'lista_fotos'),
#    (r'^documentos/(?P<slug_cat>[-\w]+)/(?P<slug_subcat>[-\w]+)/$', 'archivo_lista'),
#    (r'^documentos/(?P<slug_cat>[-\w]+)/(?P<slug_subcat>[-\w]+)/(?P<archivo_slug>[-\w]+)$', 'archivo_detalle'),
)
