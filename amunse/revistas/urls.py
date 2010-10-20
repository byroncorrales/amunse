from django.conf.urls.defaults import *
from django.conf import settings
from models import Revista

urlpatterns = patterns('revistas.views',
    (r'^revistas/$', 'revista_lista'),
    (r'^revistas/(?P<slug>[-\w]+)/$', 'revista_detalle'),
)
