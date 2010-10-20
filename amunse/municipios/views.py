# -*- coding: UTF-8 -*-
from django.http import Http404, HttpResponse
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.generic.simple import direct_to_template
from django.core.exceptions import ViewDoesNotExist
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from municipios.models import *

def municipio_detalle(request,slug):
    '''Muestra el detalle del municipio'''
    municipio = get_object_or_404(Municipio, slug=slug)
    dicc = {'m': municipio,
           }
    return direct_to_template(request, 'municipios/municipio_detalle.html',dicc)

    

