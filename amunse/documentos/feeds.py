from django.contrib.syndication.views import Feed
from models import Archivo
from amunse.tagging.models import Tag, TaggedItem
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404

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

class DocumentosBinacionalFeed(Feed):
    title = "Documentos de AMUNSE"
    link = "/documentos/binacional/feed/"
    description = 'Documentos mas recientes de AMUNSE'
    
    def items(self):
        tag = get_object_or_404(Tag, name="Binacional")
        #return Noticia.objects.filter(tags.id=tag.id)order_by('-fecha')[:10]
        #return TaggedItem.objects.filter(content_type__name='archivo', tag=tag)
        return TaggedItem.objects.get_by_model(Archivo, tag)[:10]

    def item_title(self, item):
        return item.nombre

    def item_description(self, item):
        return item.descripcion

    def item_link(self, item):
        return item.get_full_url()
