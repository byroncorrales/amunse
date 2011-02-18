from django.contrib.syndication.views import Feed
from models import Noticia
from amunse.tagging.models import Tag, TaggedItem
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404

class NoticiasFeed(Feed):
    title = "Noticias de AMUNSE"
    link = "/noticias/feed/"
    description = 'Noticias mas recientes de AMUNSE'
    
    def items(self):
        return Noticia.objects.order_by('-fecha')[:10]

    def item_title(self, item):
        return item.titulo

    def item_description(self, item):
        return item.contenido

    def item_author_name(self, item):
        return item.autor 

    def item_link(self, item):
        return item.get_full_url()

class NoticiasBinacionalFeed(Feed):
    title = "Noticias de AMUNSE"
    link = "/noticias/binacional/feed/"
    description = 'Noticias mas recientes de AMUNSE'
    
    def items(self):
        tag = get_object_or_404(Tag, name="Binacional")
        #return Noticia.objects.filter(tags=tag).order_by('-fecha')[:10]
        return TaggedItem.objects.get_by_model(Noticia, tag)[:10]

    def item_title(self, item):
        return item.titulo

    def item_description(self, item):
        return item.contenido

    def item_author_name(self, item):
        return item.autor 

    def item_link(self, item):
        return item.get_full_url()
