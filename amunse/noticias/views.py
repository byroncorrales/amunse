# -*- coding: UTF-8 -*-
from django.http import Http404, HttpResponse
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.generic.simple import direct_to_template
from django.core.exceptions import ViewDoesNotExist

from noticias.models import *

def noticia_detalle(request,slug):
    noticia = get_object_or_404(Noticia, slug=slug)
    dicc = {'noticia': noticia,
           }
    return direct_to_template(request, 'noticias/noticia_detalle.html',dicc)

def noticia_lista(request):
    noticia = Noticia.objects.all().order_by('-fecha','-id')
    dicc = {'noticia': noticia,
           }
    return direct_to_template(request, 'noticias/noticias_lista.html',dicc)
