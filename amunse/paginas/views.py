# -*- coding: UTF-8 -*-
from django.http import Http404, HttpResponse
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.generic.simple import direct_to_template
from django.core.exceptions import ViewDoesNotExist
import datetime

from paginas.models import *
from municipios.models import Municipio
from eventos.models import *
from noticias.models import *

def inicio(request):
    menu_primario = MenuPrimario.objects.all()
    menu_secundario = MenuSecundario.objects.all()
    municipio = Municipio.objects.all()
    mes_actual = datetime.datetime.now().month
    eventos = Evento.objects.filter(fecha_inicio__month = mes_actual).order_by('-fecha_inicio')[:3]
    eventos_prox = Evento.objects.filter(fecha_inicio__month = mes_actual + 1).order_by('-fecha_inicio')[:3]
    noticia = Noticia.objects.all().order_by('-fecha','-id')[:4]
    dicc = {'menu_secundario': menu_secundario,
            'menu_primario':menu_primario,
            'municipio':municipio,
            'eventos':eventos,
            'eventos_prox':eventos_prox,
            'noticia':noticia,
           }
    return direct_to_template(request, 'inicio.html',dicc)
