# -*- coding: UTF-8 -*-
from django.http import Http404, HttpResponse
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.generic.simple import direct_to_template
from django.core.exceptions import ViewDoesNotExist
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from proyectos.models import *

def proyecto_detalle(request,slug):
    '''Muestra el detalle del proyecto'''
    proyecto = get_object_or_404(Proyecto, slug=slug)
    dicc = {'proyecto': proyecto,
           }
    return direct_to_template(request, 'proyectos/proyecto_detalle.html',dicc)

def proyecto_lista(request):
    '''Vista para mostrar la lista de proyectos'''
    proyecto_lista = Proyecto.objects.all().order_by('-id')
    paginator = Paginator(proyecto_lista, 10)
    area = Area.objects.all()

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        proyecto = paginator.page(page)
    except (EmptyPage, InvalidPage):
        proyecto = paginator.page(paginator.num_pages)

    dicc = {'proyectos': proyecto,'area':area,
           }
    return direct_to_template(request, 'proyectos/proyectos_lista.html',dicc)
    
def proyecto_lista_area(request,area_slug):
    '''Filtra la lista de noticias por una categoria especifica'''
    proyecto_lista = Proyecto.objects.filter(area__slug=area_slug).order_by('-id')
    area_sel = Area.objects.get(slug=area_slug)
    area = Area.objects.all()
    paginator = Paginator(proyecto_lista, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        proyecto = paginator.page(page)
    except (EmptyPage, InvalidPage):
        proyecto = paginator.page(paginator.num_pages)

    dicc = {'proyectos': proyecto,'area':area,'area_sel':area_sel
           }
    return direct_to_template(request, 'proyectos/proyectos_lista_area.html',dicc)
