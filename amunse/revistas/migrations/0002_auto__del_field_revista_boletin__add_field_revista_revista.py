# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Revista.boletin'
        db.delete_column('revistas_revista', 'boletin')

        # Adding field 'Revista.revista'
        db.add_column('revistas_revista', 'revista', self.gf('revistas.customfilefield.ContentTypeRestrictedFileField')(default='', max_length=100), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Revista.boletin'
        db.add_column('revistas_revista', 'boletin', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100), keep_default=False)

        # Deleting field 'Revista.revista'
        db.delete_column('revistas_revista', 'revista')


    models = {
        'revistas.revista': {
            'Meta': {'object_name': 'Revista'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'edicion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('revistas.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'revista': ('revistas.customfilefield.ContentTypeRestrictedFileField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '120', 'db_index': 'True'}),
            'tags': ('tagging_autocomplete.models.TagAutocompleteField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        }
    }

    complete_apps = ['revistas']
