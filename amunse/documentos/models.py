 # -*- coding: UTF-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from tagging.fields import TagField
from tagging.models import Tag
from tagging_autocomplete.models import TagAutocompleteField

# modelos para la administracion de archivos 

class CategoriaDocumento(models.Model):
    '''Modelo que representa la categorias de primer nivel de los documentos'''
    nombre = models.CharField(max_length = 25, unique = True,blank = True, null = True)
    slug = models.SlugField(max_length = 25, unique = True,help_text = 'unico Valor',editable=False)
    descripcion = models.TextField(blank = True, null = True)

    class Meta:
        verbose_name_plural = "Categorias"

    def __unicode__(self):
        return self.nombre
    
    def save(self, force_insert=False, force_update=False):
        self.slug = slugify(self.nombre)
        super(CategoriaDocumento, self).save(force_insert, force_update)

class SubCategoriaDocumento(models.Model):
    '''Modelo que representa la categorias de segundo nivel de los documentos'''
    nombre = models.CharField(max_length = 25, unique = True,blank = True, null = True)
    slug = models.SlugField(max_length = 25, unique = True, help_text = 'unico Valor',editable=False)
    categoria = models.ForeignKey(CategoriaDocumento)

    class Meta:
        verbose_name_plural = "Sub Categorias"
        ordering = ['categoria']

    def __unicode__(self):
        return "%s - %s" % (self.categoria.nombre,self.nombre)
    
    def save(self, force_insert=False, force_update=False):
        self.slug = slugify(self.nombre)
        super(SubCategoriaDocumento, self).save(force_insert, force_update)

class Archivo(models.Model):
    '''Modelo que representa los archivos que seran subidos a la seccion de documentacion'''
    nombre = models.CharField(max_length = 200)
    fecha = models.DateField()
    descripcion = models.TextField(blank = True, null = True)
    adjunto = models.FileField(upload_to = 'attachments/documentos')
    subcategoria = models.ForeignKey(SubCategoriaDocumento) 
    slug = models.SlugField(max_length = 25, unique = True, help_text = 'unico Valor',editable=False)
    tags =  TagAutocompleteField()

    def get_absolute_url(self):
        return '%s%s/%s' % (settings.MEDIA_URL, 
                         settings.ATTACHMENT_FOLDER, self.id)
    def get_download_url(self):
        return '%s%s' % (settings.MEDIA_URL, self.adjunto)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Subir Archivos"
        
    def categoria(self):
        return self.subcategoria.categoria.nombre
    
    def save(self, force_insert=False, force_update=False):
        n = Archivo.objects.all().count()
        self.slug = str(n) + '-' + slugify(self.nombre)
        super(Archivo, self).save(force_insert, force_update)

    #Para jalar las tags
    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self, tags):
        return Tag.objects.get_for_object(self)      
