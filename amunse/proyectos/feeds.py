from django.contrib.syndication.views import Feed
from models import Proyecto

class ProyectoFeed(Feed):
    title = "Proyectos de AMUNSE"
    link = "/proyectos/feed/"
    description = 'Proyectos de AMUNSE'
    
    def items(self):
        return Proyecto.objects.all()[:10]

    def item_title(self, item):
        return item.nombre

    def item_description(self, item):
        return item.objetivos

    def item_link(self, item):
        return item.get_full_url()
