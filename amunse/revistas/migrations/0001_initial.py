# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Revista'
        db.create_table('revistas_revista', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=120, db_index=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('edicion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('imagen', self.gf('revistas.thumbs.ImageWithThumbsField')(max_length=100)),
            ('boletin', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tags', self.gf('tagging_autocomplete.models.TagAutocompleteField')()),
        ))
        db.send_create_signal('revistas', ['Revista'])


    def backwards(self, orm):
        
        # Deleting model 'Revista'
        db.delete_table('revistas_revista')


    models = {
        'revistas.revista': {
            'Meta': {'object_name': 'Revista'},
            'boletin': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'edicion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('revistas.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '120', 'db_index': 'True'}),
            'tags': ('tagging_autocomplete.models.TagAutocompleteField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        }
    }

    complete_apps = ['revistas']
