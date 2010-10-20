# -*- coding: UTF-8 -*-
from django.http import Http404, HttpResponse
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.generic.simple import direct_to_template
from django.core.exceptions import ViewDoesNotExist
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from boletines.models import *

def boletin_detalle(request,slug):
    '''Muestra el detalle de un boletín'''
    boletin = get_object_or_404(Boletin, slug=slug)
    dicc = {'boletin': boletin,
           }
    return direct_to_template(request, 'boletines/boletin_detalle.html',dicc)

def boletin_lista(request):
    '''Vista para mostrar la lista de boletines'''
    boletin_lista = Boletin.objects.all().order_by('-fecha','-id')
    paginator = Paginator(boletin_lista, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        boletin = paginator.page(page)
    except (EmptyPage, InvalidPage):
        boletin = paginator.page(paginator.num_pages)

    dicc = {'boletines': boletin,
           }
    return direct_to_template(request, 'boletines/boletines_lista.html',dicc)
    

