from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext

from models import *

def index(request):
    '''Vista general de los eventos'''
    evento_list = Evento.objects.all()
    paginator = Paginator(evento_list, 3)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        eventos = paginator.page(page)
    except (EmptyPage, InvalidPage):
        eventos = paginator.page(paginator.num_pages)

    return render_to_response('eventos/index.html', {'eventos': eventos},
                              context_instance = RequestContext(request))

def evento(request, slug):
    '''Vista de detalle'''
    evento = get_object_or_404(Evento, slug = slug)

    return render_to_response('eventos/evento.html', {'evento': evento},
                              context_instance = RequestContext(request))

def calendar(request):
    '''effin calenadar!'''
    pass
