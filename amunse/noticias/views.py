# -*- coding: UTF-8 -*-
from django.http import Http404, HttpResponse
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.generic.simple import direct_to_template
from django.core.exceptions import ViewDoesNotExist
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from noticias.models import *

def noticia_detalle(request,slug):
    '''Muestra el detalle de la noticia'''
    noticia = get_object_or_404(Noticia, slug=slug)
    #Jala las ultimas noticias relacionadas con la misma categoria y excluye a la noticia misma
    noticia_rel = Noticia.objects.filter(categoria=noticia.categoria).exclude(id = noticia.id).order_by('-fecha','-id')[:3] 
    dicc = {'noticia': noticia,
            'noticia_rel':noticia_rel,
           }
    return direct_to_template(request, 'noticias/noticia_detalle.html',dicc)

def noticia_lista(request):
    '''Vista para mostrar la lista de noticia'''
    noticia_lista = Noticia.objects.all().order_by('-fecha','-id')
    paginator = Paginator(noticia_lista, 5)
    categoria_noticia = CategoriaNoticia.objects.all()

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        noticia = paginator.page(page)
    except (EmptyPage, InvalidPage):
        noticia = paginator.page(paginator.num_pages)

    dicc = {'noticias': noticia,'categoria_noticia':categoria_noticia,
           }
    return direct_to_template(request, 'noticias/noticias_lista.html',dicc)
    
def noticia_lista_cat(request,cat_slug):
    '''Filtra la lista de noticias por una categoria especifica'''
    noticia_lista = Noticia.objects.filter(categoria__slug=cat_slug).order_by('-fecha','-id')
    categoria = CategoriaNoticia.objects.get(slug=cat_slug)
    paginator = Paginator(noticia_lista, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        noticia = paginator.page(page)
    except (EmptyPage, InvalidPage):
        noticia = paginator.page(paginator.num_pages)

    dicc = {'noticias': noticia,'categoria':categoria,
           }
    return direct_to_template(request, 'noticias/noticias_lista_cat.html',dicc)
