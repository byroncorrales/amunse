 # -*- coding: UTF-8 -*-
from django.db import models
from django.template.defaultfilters import slugify

# modelos para la administracion de archivos 

class CategoriaDocumento(models.Model):
    nombre = models.CharField(max_length = 25, unique = True,blank = True, null = True)
    slug = models.SlugField(max_length = 25, unique = True,help_text = 'unico Valor')

    class Meta:
        verbose_name_plural = "Categoria Documento"

    def __unicode__(self):
        return self.nombre

class SubCategoriaDocumento(models.Model):
    nombre = models.CharField(max_length = 25, unique = True,blank = True, null = True)
    slug = models.SlugField(max_length = 25, unique = True, help_text = 'unico Valor')
    categoria = models.ForeignKey(CategoriaDocumento)

    class Meta:
        verbose_name_plural = "Sub Categoria Documento"
        ordering = ['categoria']

    def __unicode__(self):
        return "%s - %s" % (self.nombre, self.categoria.nombre)

class Archivo(models.Model):
    nombre = models.CharField(max_length = 200)
    fecha = models.DateField()
    descripcion = models.TextField(blank = True, null = True)
    adjunto = models.FileField(upload_to = 'attachments/documentos')
    adjunto1 = models.FileField(upload_to = 'attachments/documentos',blank = True, null = True)
    adjunto2 = models.FileField(upload_to = 'attachments/documentos',blank = True, null = True)
    adjunto3 = models.FileField(upload_to = 'attachments/documentos',blank = True, null = True)
    adjunto4 = models.FileField(upload_to = 'attachments/documentos',blank = True, null = True)
    subcategoria = models.ForeignKey(SubCategoriaDocumento) 
    slug = models.SlugField(max_length = 25, unique = True, help_text = 'unico Valor',editable=False)
    def get_absolute_url(self):
        return '%s%s/%s' % (settings.MEDIA_URL, 
                         settings.ATTACHMENT_FOLDER, self.id)
    def get_download_url(self):
        return '%s%s' % (settings.MEDIA_URL, self.adjunto)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Subir Archivos"
    
    def save(self, force_insert=False, force_update=False):
        n = Archivo.objects.all().count()
        self.slug = str(n) + '-' + slugify(self.nombre)
        super(Archivo, self).save(force_insert, force_update)
