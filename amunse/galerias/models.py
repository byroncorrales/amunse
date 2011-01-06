 # -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from amunse.utils import get_file_path, get_image_path
from django.template.defaultfilters import slugify
from thumbs import ImageWithThumbsField


GALERIA_CHOICES = (
    (1, 'Fotos'),
    (2, 'Mapa'),
)

class Galeria(models.Model):
    titulo = models.CharField(max_length=160,unique = True,blank = False, null = False)
    tipo = models.IntegerField('tipo',choices=GALERIA_CHOICES)
    slug = models.SlugField(max_length = 200, unique = True,help_text = 'unico Valor',editable=False)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = "Galeria de Fotos y mapas"
        verbose_name_plural = "Galeria de fotos y mapas"
    
    def save(self, force_insert=False, force_update=False):
        self.slug = slugify(self.titulo)
        super(Galeria, self).save(force_insert, force_update)

class ImagenAdjunta(models.Model):
    titulo = models.CharField(max_length = 160)
    imagen = ImageWithThumbsField(upload_to=get_image_path, sizes=((180, 135), (135, 100), (640, 480)))
    galeria = models.ForeignKey(Galeria)
  #  slug = models.SlugField(max_length = 200, unique = True,help_text = 'unico Valor',editable=False)
    imgDir = 'attachments/imagenes/galeria'

    class Meta:
        verbose_name = "foto o mapa"
        verbose_name_plural = "fotos o mapas"

    def photo_name(self):
        return "Photo %s" % self.pk

    def image_img(self):
        if self.imagen:
            return u'<img alt="%s" title="%s" width="80" height="52" src="%s" />' % (self.photo_name(), self.photo_name(), self.imagen.url_135x100)
        else:
            return '(Without image)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True
