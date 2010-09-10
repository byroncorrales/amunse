 # -*- coding: UTF-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from tagging.fields import TagField
from tagging.models import Tag
from tagging_autocomplete.models import TagAutocompleteField
from amunse.multimedia.models import Adjunto #importando el modelo de adjuntos genericos

class CategoriaNoticia(models.Model):
    '''Modelo que representa la categorias de las noticias'''
    nombre = models.CharField('Título', max_length = 40, unique = True,blank = True, null = True)
    slug = models.SlugField(max_length = 40, unique = True,help_text = 'unico Valor',editable=False)
    
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoria de Noticia"
        verbose_name_plural = "Categorias de Noticias"

class Noticia(models.Model):
    '''Modelo que representa el tipo de contenido Noticias'''
    titulo = models.CharField('Título', max_length = 120, unique = True,blank = True, null = True)
    slug = models.SlugField(max_length = 50, unique = True,help_text = 'unico Valor',editable=False)
    fecha = models.DateField()
    contenido = models.TextField('Contenido',blank = True, null = True)
    categoria = models.ForeignKey(CategoriaNoticia)
    tags =  TagAutocompleteField()
    adjunto = generic.GenericRelation(Adjunto)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
    
    def save(self, force_insert=False, force_update=False):
        n = Noticia.objects.all().count()
        self.slug = str(n) + '-' + slugify(self.titulo)
        super(Noticia, self).save(force_insert, force_update)

    #Para jalar las tags
    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self, tags):
        return Tag.objects.get_for_object(self)  

