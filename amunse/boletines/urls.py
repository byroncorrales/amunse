from django.conf.urls.defaults import *
from django.conf import settings
from models import Boletin

urlpatterns = patterns('boletines.views',
    (r'^boletines/$', 'boletin_lista'),
    (r'^boletines/(?P<slug>[-\w]+)/$', 'boletin_detalle'),
)
