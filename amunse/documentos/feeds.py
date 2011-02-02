from django.contrib.syndication.views import Feed
from models import Archivo

class DocumentosFeed(Feed):
    title = "Documentos de AMUNSE"
    link = "/documentos/feed/"
    description = 'Documentos mas recientes de AMUNSE'
    
    def items(self):
        return Archivo.objects.order_by('-fecha')[:10]

    def item_title(self, item):
        return item.nombre

    def item_description(self, item):
        return item.descripcion

    def item_link(self, item):
        return item.get_full_url()
