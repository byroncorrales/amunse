# -*- coding: UTF-8 -*-
import datetime
from django.core.exceptions import ViewDoesNotExist
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.defaultfilters import slugify
from django.views.generic.simple import direct_to_template
from eventos.models import *
from municipios.models import Municipio
from noticias.models import *
from paginas.models import *
from tagging.models import *

def inicio(request):
    mes_actual = datetime.datetime.now().month
    eventos = Evento.objects.filter(fecha_inicio__month=mes_actual).order_by('-fecha_inicio')[:3]
    eventos_prox = Evento.objects.filter(fecha_inicio__month=mes_actual + 1).order_by('-fecha_inicio')[:3]
    noticia = Noticia.objects.all().order_by('-fecha', '-id')[:4]
    dicc = {
        'eventos':eventos,
        'eventos_prox':eventos_prox,
        'noticia':noticia,
    }
    return render_to_response('inicio.html', dicc,
                              context_instance=RequestContext(request))

def tags(request, id):
    tag = get_object_or_404(Tag, pk=int(id))
    objects = TaggedItem.objects.filter(tag=tag)
    return render_to_response('tags.html', RequestContext(request, locals()))

def pagina(request,slug):
    '''Muestra el detalle de la pagina'''
    pagina = get_object_or_404(Pagina, slug=slug)
    #Jala las ultimas noticias relacionadas con la misma categoria y excluye a la noticia misma
    dicc = {'pagina': pagina,
           }
    return direct_to_template(request, 'paginas/pagina_detalle.html',dicc)
