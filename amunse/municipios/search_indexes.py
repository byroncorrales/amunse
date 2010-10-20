from haystack.indexes import *
from haystack import site
from models import Municipio 
import datetime

class MunicipioIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    titulo = CharField(model_attr='nombre')

    def get_queryset(self):
        return Municipio.objects.all()

site.register(Municipio, MunicipioIndex)
