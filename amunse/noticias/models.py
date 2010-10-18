    # -*- coding: UTF-8 -*-
from amunse.multimedia.models import Adjunto
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.template.defaultfilters import slugify
from south.modelsinspector import add_introspection_rules
from tagging.fields import TagField
from tagging.models import Tag
from tagging_autocomplete.models import TagAutocompleteField
from thumbs import ImageWithThumbsField
add_introspection_rules = ([], ["^tagging_autocomplete\.models\.TagAutocompleteField"]) 

class CategoriaNoticia(models.Model):
    '''Modelo que representa la categorias de las noticias'''
    nombre = models.CharField('Título', max_length=40, unique=True, blank=True, null=True)
    slug = models.SlugField(max_length=40, unique=True, help_text='unico Valor', editable=False)
    
    def __unicode__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False):
        self.slug = slugify(self.nombre)
        super(CategoriaNoticia, self).save(force_insert, force_update)

    class Meta:
        verbose_name = "Categoria de Noticia"
        verbose_name_plural = "Categorias de Noticias"


class Noticia(models.Model):
    '''Modelo que representa el tipo de contenido Noticias'''
    titulo = models.CharField('Título', max_length=120, unique=True, blank=False, null=False)
    slug = models.SlugField(max_length=120, unique=True, help_text='unico Valor', editable=False)
    fecha = models.DateField()
    autor = models.CharField('Autor', max_length=100, blank=True, null=True)
    categoria = models.ForeignKey(CategoriaNoticia)
    imagen = ImageWithThumbsField(upload_to='attachments/imagenes', sizes=((178, 90), (255, 190)))
    contenido = models.TextField('Contenido', blank=True, null=True)
    tags = TagAutocompleteField(help_text='Separar elementos con "," ')
    adjunto = generic.GenericRelation(Adjunto)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
    
    def save(self, force_insert=False, force_update=False):
        try:
            Noticia.objects.get(pk=self.id)            
        except:
            n = Noticia.objects.all().count()
            self.slug = str(n) + '-' + slugify(self.titulo)
        super(Noticia, self).save(force_insert, force_update)

    #Para jalar las tags
    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self):
        return Tag.objects.get_for_object(self)

    #metodo para devolver la url exacta del objeto
    def get_full_url(self):
        return "/noticias/%s/" % self.slug

    #metodo para obtener el nombre del objeto
    def get_name(self):
        return self.titulo
    
#    def categorias(self):
#        return self.Noticia.all()[0].categoria.nombre

class Comentario(models.Model):
    '''Modelo que representa los comentarios de las noticias'''
    noticia = models.ForeignKey(Noticia)
    fecha = models.DateField()
    estado = models.BooleanField('Publicado', blank=False, null=False)
    nombre = models.CharField('Nombre', max_length=120, blank=False, null=False)
    correo = models.EmailField('Correo', blank=True, null=True)
    contenido = models.TextField('Contenido', blank=True, null=True)


    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"


