# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Boletin.boletin'
        db.alter_column('boletines_boletin', 'boletin', self.gf('boletines.customfilefield.ContentTypeRestrictedFileField')(max_length=100))


    def backwards(self, orm):
        
        # Changing field 'Boletin.boletin'
        db.alter_column('boletines_boletin', 'boletin', self.gf('django.db.models.fields.files.FileField')(max_length=100))


    models = {
        'boletines.boletin': {
            'Meta': {'object_name': 'Boletin'},
            'boletin': ('boletines.customfilefield.ContentTypeRestrictedFileField', [], {'max_length': '100'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'edicion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('boletines.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '120', 'db_index': 'True'}),
            'tags': ('tagging_autocomplete.models.TagAutocompleteField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        }
    }

    complete_apps = ['boletines']
