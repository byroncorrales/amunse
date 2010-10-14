from django.conf.urls.defaults import *
from django.conf import settings
from models import Pagina

urlpatterns = patterns('paginas.views',
    (r'^index/$', 'inicio'),
)
