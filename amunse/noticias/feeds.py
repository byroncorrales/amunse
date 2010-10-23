from django.contrib.syndication.views import Feed
from models import Noticia


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
