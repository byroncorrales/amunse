from django.conf.urls.defaults import *
from django.conf import settings
from models import Proyecto
from feeds import ProyectoFeed

urlpatterns = patterns('proyectos.views',
    (r'^proyectos/feed/$', ProyectoFeed()),
    (r'^proyectos/(?P<slug>[-\w]+)/$', 'proyecto_detalle'),
    (r'^proyectos/area/(?P<area_slug>[-\w]+)/$', 'proyecto_lista_area'),
    (r'^proyectos/$', 'proyecto_lista'),
)
