# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Archivo.slug'
        db.delete_column('documentos_archivo', 'slug')


    def backwards(self, orm):
        
        # Adding field 'Archivo.slug'
        db.add_column('documentos_archivo', 'slug', self.gf('django.db.models.fields.SlugField')(default=None, max_length=50, unique=True, db_index=True), keep_default=False)


    models = {
        'documentos.archivo': {
            'Meta': {'ordering': "['-fecha']", 'object_name': 'Archivo'},
            'adjunto': ('amunse.documentos.customfilefield.ContentTypeRestrictedFileField', [], {'max_length': '100'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'subcategoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documentos.SubCategoriaDocumento']"}),
            'tags': ('tagging_autocomplete.models.TagAutocompleteField', [], {'max_length': '255', 'blank': 'True'})
        },
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
        }
    }

    complete_apps = ['documentos']
