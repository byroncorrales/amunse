# -*- coding: UTF-8 -*-
from django.http import Http404, HttpResponse
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.generic.simple import direct_to_template
from django.core.exceptions import ViewDoesNotExist

from models import *

def lista(request,tipo_gal):
    '''Vista para mostrar la lista de galerias'''
    galeria_lista = Galeria.objects.filter(tipo=tipo_gal).order_by('titulo')
    fotos = ImagenAdjunta.objects.filter(galeria__tipo = tipo_gal)
    if int(tipo_gal) == 1:
        tipo = "Galeria de Fotos"
    else:
        tipo = "Galeria de Mapas"
    
    dicc = {'galeria_lista': galeria_lista, 'tipo':tipo, 'fotos':fotos,
           }
    return direct_to_template(request, 'galerias/galeria_lista.html',dicc)

def lista_fotos(request,tipo_gal,slug):
    '''vista para mostrar la lista de fotos de una galeria'''
    fotos = ImagenAdjunta.objects.filter(galeria__slug=slug)
    galeria = Galeria.objects.get(slug=slug)
    dicc = {'fotos': fotos,'galeria':galeria
           }
    return direct_to_template(request, 'galerias/galeria_detalle.html',dicc)
