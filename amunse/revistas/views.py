# -*- coding: UTF-8 -*-
from django.http import Http404, HttpResponse
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.generic.simple import direct_to_template
from django.core.exceptions import ViewDoesNotExist
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from revistas.models import *

def revista_detalle(request,slug):
    '''Muestra el detalle de la revista'''
    revista = get_object_or_404(Revista, slug=slug)
    dicc = {'revista': revista,
           }
    return direct_to_template(request, 'revistas/revista_detalle.html',dicc)

def revista_lista(request):
    '''Vista para mostrar la lista de revistas'''
    revista_lista = Revista.objects.all().order_by('-fecha','-id')
    paginator = Paginator(revista_lista, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        revista = paginator.page(page)
    except (EmptyPage, InvalidPage):
        revista = paginator.page(paginator.num_pages)

    dicc = {'revistas': revista,
           }
    return direct_to_template(request, 'revistas/revista_lista.html',dicc)
    

