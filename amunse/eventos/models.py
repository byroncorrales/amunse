 # -*- coding: UTF-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from tagging.fields import TagField
from tagging.models import Tag
from tagging_autocomplete.models import TagAutocompleteField
from amunse.multimedia.models import Adjunto #importando el modelo de adjuntos genericos

# Regla para que funcionen las migraciones de south con los campos de django-tagging
from south.modelsinspector import add_introspection_rules
add_introspection_rules = ([], ["^tagging_autocomplete\.models\.TagAutocompleteField"]) 

class Evento(models.Model):
    '''Modelo que representa el tipo de contenido Noticias'''
    titulo = models.CharField('Título', max_length = 120, unique = True,blank = False, null = False)
    slug = models.SlugField(max_length = 120, unique = True,help_text = 'unico Valor',editable=False)
    fecha_inicio = models.DateField('Fecha de Inicio',blank = False, null = False)
    fecha_final = models.DateField('Fecha Final',blank = False, null = False)
    Lugar = models.CharField('Lugar', max_length = 150,blank = True, null = True)
    contenido = models.TextField('Contenido',blank = True, null = True)
    tags =  TagAutocompleteField(help_text='Separar elementos con "," ')
    adjunto = generic.GenericRelation(Adjunto)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
    
    def save(self, force_insert=False, force_update=False):
        try:
            Evento.objects.get(pk=self.id)
        except:
            n = Evento.objects.all().count()
            self.slug = str(n) + '-' + slugify(self.titulo)
        super(Evento, self).save(force_insert, force_update)

    #Para jalar las tags
    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self, tags):
        return Tag.objects.get_for_object(self)  
