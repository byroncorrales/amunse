from django.conf.urls.defaults import *
from django.conf import settings
from models import Municipio

urlpatterns = patterns('municipios.views',
    (r'^municipios/(?P<slug>[-\w]+)/$', 'municipio_detalle'),
)
