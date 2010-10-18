# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Evento.Lugar'
        db.delete_column('eventos_evento', 'Lugar')

        # Adding field 'Evento.lugar'
        db.add_column('eventos_evento', 'lugar', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True), keep_default=False)

        # Changing field 'Evento.fecha_final'
        db.alter_column('eventos_evento', 'fecha_final', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Evento.fecha_inicio'
        db.alter_column('eventos_evento', 'fecha_inicio', self.gf('django.db.models.fields.DateTimeField')())


    def backwards(self, orm):
        
        # Adding field 'Evento.Lugar'
        db.add_column('eventos_evento', 'Lugar', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True), keep_default=False)

        # Deleting field 'Evento.lugar'
        db.delete_column('eventos_evento', 'lugar')

        # Changing field 'Evento.fecha_final'
        db.alter_column('eventos_evento', 'fecha_final', self.gf('django.db.models.fields.DateField')())

        # Changing field 'Evento.fecha_inicio'
        db.alter_column('eventos_evento', 'fecha_inicio', self.gf('django.db.models.fields.DateField')())


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'eventos.evento': {
            'Meta': {'object_name': 'Evento'},
            'contenido': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_final': ('django.db.models.fields.DateTimeField', [], {}),
            'fecha_inicio': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '120', 'db_index': 'True'}),
            'tags': ('tagging_autocomplete.models.TagAutocompleteField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
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

    complete_apps = ['eventos']
