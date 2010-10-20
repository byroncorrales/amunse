from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import *
from models import *

@login_required(redirect_field_name='next')
def subir_imagen(request):
    if request.method == 'POST':
        form = AdjuntaForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            if 'imagen' in request.FILES:
                new = ImagenAdjunta()
                new.imagen = request.FILES['imagen']
                new.save()
                imagen = new
    else:
        form = AdjuntaForm()

    #metodo para borrar la imagen si presionas el boton cancelar
    if request.is_ajax():
        id = request.POST['id']
        obj = ImagenAdjunta.objects.get(pk=int(id))
        obj.delete()

    return render_to_response('multimedia/huerfana.html', RequestContext(request, locals()))

