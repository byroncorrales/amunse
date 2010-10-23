 # -*- coding: UTF-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from tagging.fields import TagField
from tagging.models import *
from tagging_autocomplete.models import TagAutocompleteField
from customfilefield import ContentTypeRestrictedFileField
# Regla para que funcionen las migraciones de south con los campos de django-tagging
from south.modelsinspector import add_introspection_rules
add_introspection_rules = ([], ["^tagging_autocomplete\.models\.TagAutocompleteField"]) 

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
#    adjunto = models.FileField(upload_to = 'attachments/documentos')
    adjunto = ContentTypeRestrictedFileField(upload_to = 'attachments/documentos', content_types=['application/pdf', 'application/zip','application/vnd.ms-powerpoint','application/vnd.ms-excel','application/msword','application/vnd.oasis.opendocument.text','application/vnd.oasis.opendocument.spreadsheet','application/vnd.oasis.opendocument.presentation'],max_upload_size=12582912, help_text='Solo se permiten archivos .doc .xls .ppt .docx .xlsx .pptx .pdf .zip .odp .odt .ods , tamaño máximo 12MB')
    subcategoria = models.ForeignKey(SubCategoriaDocumento) 
    slug = models.SlugField(max_length = 25, unique = True, help_text = 'unico Valor',editable=False)
    tags =  TagAutocompleteField(help_text='Separar elementos con "," ')

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
        try:
            Archivo.objects.get(pk=self.id)
        except:
            n = Archivo.objects.all().count()
            self.slug = str(n) + '-' + slugify(self.nombre)
        super(Archivo, self).save(force_insert, force_update)

    #Para jalar las tags
    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self, tags):
        return Tag.objects.get_for_object(self)

    #metodo url del objeto
    def get_full_url(self):
        return "/documentos/%s/" % self.slug

    #metodo para obtener el nombre del objeto
    def get_name(self):
        return self.nombre
