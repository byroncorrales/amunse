# -*- coding: UTF-8 -*-
# extra.py in yourproject/app/

from django.db.models import FileField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
import mimetypes

class ContentTypeRestrictedFileField(FileField):
    """
    Same as FileField, but you can specify:
        * content_types - list containing allowed content_types. Example: ['application/pdf', 'image/jpeg']
        * max_upload_size - a number indicating the maximum file size allowed for upload.
            2.5MB - 2621440
            5MB - 5242880
            10MB - 10485760
            20MB - 20971520
            50MB - 5242880
            100MB 104857600
            250MB - 214958080
            500MB - 429916160
    """
    def __init__(self, content_types=None, max_upload_size=None, **kwargs):
        self.content_types = content_types
        self.max_upload_size = max_upload_size
        super(ContentTypeRestrictedFileField, self).__init__(**kwargs)
#    def __init__(self, *args, **kwargs):
#        self.content_types = kwargs.pop("content_types")
#        self.max_upload_size = kwargs.pop("max_upload_size")

#        super(ContentTypeRestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, * args, ** kwargs):
        data = super(ContentTypeRestrictedFileField, self).clean(*args, ** kwargs)
        file = data.file        
        try:
            content_type = file.content_type
            bandera = 0
        except:
            bandera = 1            
            content_type = mimetypes.guess_type(str(file))[0]

        if content_type in self.content_types:
            if bandera == 0:
                if file._size > self.max_upload_size:
                    raise forms.ValidationError(_('El Archivo debe ser menor a %s. El archivo actual es de %s') % (filesizeformat(self.max_upload_size), filesizeformat(file._size)))
            return data
        else:
            raise forms.ValidationError(_('Archivo no soportado.'))

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^documentos\.customfilefield\.ContentTypeRestrictedFileField"])
