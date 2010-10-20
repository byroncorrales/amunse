from haystack.indexes import *
from haystack import site
from models import Proyecto 
import datetime

class ProyectoIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    titulo = CharField(model_attr='nombre')
    fecha = DateField(model_attr='fecha_inicial')

    def get_queryset(self):
        return Proyecto.objects.filter(fecha_inicio__lte=datetime.datetime.now())

site.register(Proyecto, ProyectoIndex)
