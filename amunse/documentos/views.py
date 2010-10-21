# -*- coding: UTF-8 -*-
from django.http import Http404, HttpResponse
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.generic.simple import direct_to_template
from django.core.exceptions import ViewDoesNotExist
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from models import *

def categoria_lista(request):
    '''Vista para mostrar la lista de categorias de documentos'''
    categoria_lista = CategoriaDocumento.objects.all().order_by('nombre')
    
    dicc = {'categoria': categoria_lista,
           }
    return direct_to_template(request, 'documentos/categorias_lista.html',dicc)

def subcategoria_lista(request,slug_cat):
    '''Muestra la lista de subcategorias de documentos'''
    subcategoria_lista = SubCategoriaDocumento.objects.filter(categoria__slug=slug_cat).order_by('nombre')
    categoria = get_object_or_404(CategoriaDocumento, slug=slug_cat)
    dicc = {'subcategoria': subcategoria_lista, 'categoria':categoria,
           }
    return direct_to_template(request, 'documentos/subcategorias_lista.html',dicc)

def archivo_lista(request,slug_cat, slug_subcat):
    '''Muestra la lista de archivos basado en una subcategoria'''
    archivo_lista = Archivo.objects.filter(subcategoria__slug=slug_subcat).order_by('nombre')
    subcategoria = get_object_or_404(SubCategoriaDocumento, slug=slug_subcat)
    dicc = {'archivo': archivo_lista, 'subcategoria':subcategoria,
           }
    return direct_to_template(request, 'documentos/archivos_lista.html',dicc)
