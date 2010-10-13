from paginas.models import *
from municipios.models import Municipio

def elementos_fijos(request):
    #TODO: cache
    menu_primario = MenuPrimario.objects.all()
    menu_secundario = MenuSecundario.objects.all()
    municipio = Municipio.objects.all()
    dicc = {
            'menu_secundario': menu_secundario,
            'menu_primario':menu_primario,
            'municipio':municipio,
           }
    return dicc
