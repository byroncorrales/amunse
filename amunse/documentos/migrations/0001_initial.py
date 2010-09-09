# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CategoriaDocumento'
        db.create_table('documentos_categoriadocumento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=25, unique=True, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=25, db_index=True)),
        ))
        db.send_create_signal('documentos', ['CategoriaDocumento'])

        # Adding model 'SubCategoriaDocumento'
        db.create_table('documentos_subcategoriadocumento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=25, unique=True, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=25, db_index=True)),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documentos.CategoriaDocumento'])),
        ))
        db.send_create_signal('documentos', ['SubCategoriaDocumento'])

        # Adding model 'Archivo'
        db.create_table('documentos_archivo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('adjunto', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('adjunto1', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('adjunto2', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('adjunto3', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('adjunto4', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('subcategoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documentos.SubCategoriaDocumento'])),
        ))
        db.send_create_signal('documentos', ['Archivo'])


    def backwards(self, orm):
        
        # Deleting model 'CategoriaDocumento'
        db.delete_table('documentos_categoriadocumento')

        # Deleting model 'SubCategoriaDocumento'
        db.delete_table('documentos_subcategoriadocumento')

        # Deleting model 'Archivo'
        db.delete_table('documentos_archivo')


    models = {
        'documentos.archivo': {
            'Meta': {'object_name': 'Archivo'},
            'adjunto': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'adjunto1': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'adjunto2': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'adjunto3': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'adjunto4': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subcategoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documentos.SubCategoriaDocumento']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'documentos.categoriadocumento': {
            'Meta': {'object_name': 'CategoriaDocumento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '25', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '25', 'db_index': 'True'})
        },
        'documentos.subcategoriadocumento': {
            'Meta': {'object_name': 'SubCategoriaDocumento'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documentos.CategoriaDocumento']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '25', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '25', 'db_index': 'True'})
        }
    }

    complete_apps = ['documentos']
