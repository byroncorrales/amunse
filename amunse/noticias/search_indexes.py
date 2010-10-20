from haystack.indexes import *
from haystack import site
from models import Noticia 
import datetime

class NoticiaIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    titulo = CharField(model_attr='title')
    fecha = DateField(model_attr='fecha')

    def get_queryset(self):
        return Noticia.objects.filter(fecha__lte=datetime.datetime.now())

site.register(Noticia, NoticiaIndex)
