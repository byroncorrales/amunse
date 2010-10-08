# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'MenuPrimario.imagen'
        db.add_column('paginas_menuprimario', 'imagen', self.gf('paginas.thumbs.ImageWithThumbsField')(default='', max_length=100), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'MenuPrimario.imagen'
        db.delete_column('paginas_menuprimario', 'imagen')


    models = {
        'paginas.menuprimario': {
            'Meta': {'object_name': 'MenuPrimario'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('paginas.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
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
            'url': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'})
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
