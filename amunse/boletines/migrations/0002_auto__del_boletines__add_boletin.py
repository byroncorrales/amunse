# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Boletines'
        db.delete_table('boletines_boletines')

        # Adding model 'Boletin'
        db.create_table('boletines_boletin', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=120, db_index=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('imagen', self.gf('boletines.thumbs.ImageWithThumbsField')(max_length=100)),
            ('boletin', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tags', self.gf('tagging_autocomplete.models.TagAutocompleteField')()),
        ))
        db.send_create_signal('boletines', ['Boletin'])


    def backwards(self, orm):
        
        # Adding model 'Boletines'
        db.create_table('boletines_boletines', (
            ('boletin', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('tags', self.gf('tagging_autocomplete.models.TagAutocompleteField')()),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=120, unique=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=120, unique=True, db_index=True)),
        ))
        db.send_create_signal('boletines', ['Boletines'])

        # Deleting model 'Boletin'
        db.delete_table('boletines_boletin')


    models = {
        'boletines.boletin': {
            'Meta': {'object_name': 'Boletin'},
            'boletin': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('boletines.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '120', 'db_index': 'True'}),
            'tags': ('tagging_autocomplete.models.TagAutocompleteField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        }
    }

    complete_apps = ['boletines']
