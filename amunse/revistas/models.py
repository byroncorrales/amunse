 # -*- coding: UTF-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from tagging.fields import TagField
from tagging.models import Tag
from thumbs import ImageWithThumbsField
from tagging_autocomplete.models import TagAutocompleteField

# Regla para que funcionen las migraciones de south con los campos de django-tagging
from south.modelsinspector import add_introspection_rules
add_introspection_rules = ([], ["^tagging_autocomplete\.models\.TagAutocompleteField"]) 

class Revista(models.Model):
    '''Modelo que representa el tipo de contenido para las revistas'''
    titulo = models.CharField('Título', max_length = 120, unique = True,blank = False, null = False)
    slug = models.SlugField(max_length = 120, unique = True,help_text = 'unico Valor',editable=False)
    fecha = models.DateField('Fecha',blank = False, null = False)
    edicion = models.IntegerField('Número de edición',blank = True, null = True)
    imagen = ImageWithThumbsField('Imagen portada',upload_to='attachments/imagenes', sizes=((80,100),(190,230)), help_text="Imágen de portada")
    boletin = models.FileField('Revista Adjunto',upload_to = 'attachments/revistas')
    descripcion = models.TextField('Descripción',blank = True, null = True)
    tags =  TagAutocompleteField(help_text='Separar elementos con "," ')

    def __unicode__(self):
        return self.titulo

    def get_absolute_url(self):
        return '%s%s/%s' % (settings.MEDIA_URL, 
                         settings.ATTACHMENT_FOLDER, self.id)
    def get_download_url(self):
        return '%s%s' % (settings.MEDIA_URL, self.adjunto)
        
    class Meta:
        verbose_name = "Revista"
        verbose_name_plural = "Revistas"
    
    def save(self, force_insert=False, force_update=False):
        try:
            Revista.objects.get(pk=self.id)
        except:
            n = Revista.objects.all().count()
            self.slug = str(n) + '-' + slugify(self.titulo)
        super(Revista, self).save(force_insert, force_update)

    #Para jalar las tags
    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self, tags):
        return Tag.objects.get_for_object(self)  
