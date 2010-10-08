# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Adjunto.adjunto'
        db.alter_column('multimedia_adjunto', 'adjunto', self.gf('amunse.multimedia.customfilefield.ContentTypeRestrictedFileField')(max_length=100))


    def backwards(self, orm):
        
        # Changing field 'Adjunto.adjunto'
        db.alter_column('multimedia_adjunto', 'adjunto', self.gf('django.db.models.fields.files.FileField')(max_length=100))


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'multimedia.adjunto': {
            'Meta': {'object_name': 'Adjunto'},
            'adjunto': ('amunse.multimedia.customfilefield.ContentTypeRestrictedFileField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['multimedia']
