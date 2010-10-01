# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'MenuSecundario.pagina'
        db.add_column('paginas_menusecundario', 'pagina', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['paginas.Pagina'], null=True, blank=True), keep_default=False)

        # Changing field 'MenuSecundario.menuprimario'
        db.alter_column('paginas_menusecundario', 'menuprimario_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['paginas.MenuPrimario']))


    def backwards(self, orm):
        
        # Deleting field 'MenuSecundario.pagina'
        db.delete_column('paginas_menusecundario', 'pagina_id')

        # Changing field 'MenuSecundario.menuprimario'
        db.alter_column('paginas_menusecundario', 'menuprimario_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['paginas.MenuPrimario'], null=True))


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
            'adjunto': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'paginas.menuprimario': {
            'Meta': {'object_name': 'MenuPrimario'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orden': ('django.db.models.fields.IntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '120', 'db_index': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        },
        'paginas.menusecundario': {
            'Meta': {'object_name': 'MenuSecundario'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menuprimario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['paginas.MenuPrimario']"}),
            'orden': ('django.db.models.fields.IntegerField', [], {}),
            'pagina': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['paginas.Pagina']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '120', 'db_index': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'paginas.pagina': {
            'Meta': {'object_name': 'Pagina'},
            'contenido': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '120', 'db_index': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        }
    }

    complete_apps = ['paginas']
