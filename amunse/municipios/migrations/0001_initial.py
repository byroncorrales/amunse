# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Municipio'
        db.create_table('municipios_municipio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=120, db_index=True)),
            ('caracterizacion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('ubicacion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('historia', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('documentacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documentos.SubCategoriaDocumento'])),
        ))
        db.send_create_signal('municipios', ['Municipio'])


    def backwards(self, orm):
        
        # Deleting model 'Municipio'
        db.delete_table('municipios_municipio')


    models = {
        'documentos.categoriadocumento': {
            'Meta': {'object_name': 'CategoriaDocumento'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '25', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '25', 'db_index': 'True'})
        },
        'documentos.subcategoriadocumento': {
            'Meta': {'ordering': "['categoria']", 'object_name': 'SubCategoriaDocumento'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documentos.CategoriaDocumento']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '25', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '25', 'db_index': 'True'})
        },
        'municipios.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'caracterizacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'documentacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documentos.SubCategoriaDocumento']"}),
            'historia': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '120', 'db_index': 'True'}),
            'ubicacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['municipios']
