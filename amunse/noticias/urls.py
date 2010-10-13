from django.conf.urls.defaults import *
from django.conf import settings
from models import Noticia

urlpatterns = patterns('noticias.views',
    (r'^noticias/(?P<slug>[-\w]+)/$', 'noticia_detalle'),
)
