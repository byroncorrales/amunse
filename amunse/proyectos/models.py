 # -*- coding: UTF-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from thumbs import ImageWithThumbsField
from tagging.fields import TagField
from tagging.models import *
from tagging_autocomplete.models import TagAutocompleteField
# Regla para que funcionen las migraciones de south con los campos de django-tagging
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^amunse\.tagging_autocomplete\.models\.TagAutocompleteField"])

ESTADO_CHOICES = (
    (1, 'En Desarrollo'),
    (2, 'Terminado'),
    (3, 'En Gestión'),
)

class Financiador(models.Model):
    nombre = models.CharField('Financiador', max_length = 150,unique = True,blank = False, null = False)
    slug = models.SlugField(max_length = 150, unique = True,help_text = 'unico Valor',editable=False)
    logo = ImageWithThumbsField(upload_to='attachments/logos', sizes=((150,150),(250,250)), blank = True, null = True)
    enlace = models.URLField('Enlace',verify_exists=True,blank = True, null = True, help_text='ej: http://www.amunse.org.ni')

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Financiador"
        verbose_name_plural = "Financiadores"
    
    def save(self, force_insert=False, force_update=False):
        self.slug = slugify(self.nombre)
        super(Financiador, self).save(force_insert, force_update)
        
class Area(models.Model):
    nombre = models.CharField('Área', max_length = 150,unique = True,blank = False, null = False)
    slug = models.SlugField(max_length = 150, unique = True,help_text = 'unico Valor',editable=False)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"
    
    def save(self, force_insert=False, force_update=False):
        self.slug = slugify(self.nombre)
        super(Area, self).save(force_insert, force_update)

class Proyecto(models.Model):
    '''Modelo que representa el tipo de contenido para los proyectos'''
    nombre = models.CharField('Nombre', max_length = 200, unique = True,blank = False, null = False)
    slug = models.SlugField(max_length = 200, unique = True,help_text = 'unico Valor',editable=False)
    monto = models.DecimalField('Monto $',max_digits=10, decimal_places=2, blank = True, null = True, help_text= 'No usar "," para separación de miles')
    lugar = models.CharField('Lugar', max_length = 200, blank = True, null = True)
    fecha_inicio = models.DateField('Fecha de inicio',blank = True, null = True)
    fecha_final = models.DateField('Fecha final',blank = True, null = True)
    estado = models.IntegerField('Estado actual',choices=ESTADO_CHOICES)
    area = models.ManyToManyField(Area, verbose_name ='Areas institucionales')
    financiador = models.ManyToManyField(Financiador, verbose_name ='Financiadores')
    objetivos = models.TextField('Objetivos',blank = True, null = True)
    resultados = models.TextField('Resultados',blank = True, null = True)
    tags =  TagAutocompleteField(help_text='Separar elementos con "," ')

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-id']
    
    def save(self, force_insert=False, force_update=False):
        self.slug = slugify(self.nombre)
        super(Proyecto, self).save(force_insert, force_update)

    def get_full_url(self):
        return "/proyectos/%s/" % self.slug
