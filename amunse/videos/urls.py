from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('videos.views',
                      (r'^$', 'index'),
)
