# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Galeria'
        db.create_table('galerias_galeria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=160)),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200, db_index=True)),
        ))
        db.send_create_signal('galerias', ['Galeria'])

        # Adding model 'ImagenAdjunta'
        db.create_table('galerias_imagenadjunta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=160)),
            ('imagen', self.gf('amunse.galerias.thumbs.ImageWithThumbsField')(max_length=100)),
            ('galeria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['galerias.Galeria'])),
        ))
        db.send_create_signal('galerias', ['ImagenAdjunta'])


    def backwards(self, orm):
        
        # Deleting model 'Galeria'
        db.delete_table('galerias_galeria')

        # Deleting model 'ImagenAdjunta'
        db.delete_table('galerias_imagenadjunta')


    models = {
        'galerias.galeria': {
            'Meta': {'object_name': 'Galeria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '160'})
        },
        'galerias.imagenadjunta': {
            'Meta': {'object_name': 'ImagenAdjunta'},
            'galeria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['galerias.Galeria']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('amunse.galerias.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '160'})
        }
    }

    complete_apps = ['galerias']
