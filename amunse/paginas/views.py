# -*- coding: UTF-8 -*-
from django.http import Http404, HttpResponse
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.generic.simple import direct_to_template
from django.core.exceptions import ViewDoesNotExist

from paginas.models import *
from municipios.models import Municipio

def inicio(request):
    menu_primario = MenuPrimario.objects.all()
    menu_secundario = MenuSecundario.objects.all()
    municipio = Municipio.objects.all()
    dicc = {'menu_secundario': menu_secundario,
            'menu_primario':menu_primario,
            'municipio':municipio,
           }
    return direct_to_template(request, 'inicio.html',dicc)
