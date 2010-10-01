 # -*- coding: UTF-8 -*-
from django.db import models
from thumbs import ImageWithThumbsField


class Banner(models.Model):
    nombre = models.CharField(max_length = 150)
    imagen = ImageWithThumbsField(upload_to='attachments/banners', sizes=((400,120),))

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"
