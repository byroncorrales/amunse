# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext

from models import *


def index(request):
    '''vista de indice lista de videos paginados'''
    video_list = Video.objects.all().order_by('-fecha','-id')
    paginator = Paginator(video_list, 3)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        videos = paginator.page(page)
    except (EmptyPage, InvalidPage):
        videos = paginator.page(paginator.num_pages)

    return render_to_response('videos/index.html', {'videos': videos},
                              context_instance = RequestContext(request))

def video_popup(request, id):
    '''vista para el pocup del video'''
    video = get_object_or_404(Video, id=id)
    return render_to_response('videos/video_popup.html', {'video': video},
                              context_instance = RequestContext(request))
                              
def video_detalle(request, slug):
    '''vista detalle del video'''
    video = get_object_or_404(Video, slug=slug)
    return render_to_response('videos/video_detalle.html', {'video': video},
                              context_instance = RequestContext(request))
