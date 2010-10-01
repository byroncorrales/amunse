# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Financiador'
        db.create_table('proyectos_financiador', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150, db_index=True)),
            ('logo', self.gf('proyectos.thumbs.ImageWithThumbsField')(max_length=100)),
            ('enlace', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('proyectos', ['Financiador'])

        # Adding model 'Area'
        db.create_table('proyectos_area', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150, db_index=True)),
        ))
        db.send_create_signal('proyectos', ['Area'])

        # Adding model 'Proyecto'
        db.create_table('proyectos_proyecto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200, db_index=True)),
            ('monto', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('lugar', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('fecha_inicio', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('estado', self.gf('django.db.models.fields.IntegerField')()),
            ('objetivos', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('resultados', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('proyectos', ['Proyecto'])

        # Adding M2M table for field area on 'Proyecto'
        db.create_table('proyectos_proyecto_area', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyecto', models.ForeignKey(orm['proyectos.proyecto'], null=False)),
            ('area', models.ForeignKey(orm['proyectos.area'], null=False))
        ))
        db.create_unique('proyectos_proyecto_area', ['proyecto_id', 'area_id'])

        # Adding M2M table for field financiador on 'Proyecto'
        db.create_table('proyectos_proyecto_financiador', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyecto', models.ForeignKey(orm['proyectos.proyecto'], null=False)),
            ('financiador', models.ForeignKey(orm['proyectos.financiador'], null=False))
        ))
        db.create_unique('proyectos_proyecto_financiador', ['proyecto_id', 'financiador_id'])


    def backwards(self, orm):
        
        # Deleting model 'Financiador'
        db.delete_table('proyectos_financiador')

        # Deleting model 'Area'
        db.delete_table('proyectos_area')

        # Deleting model 'Proyecto'
        db.delete_table('proyectos_proyecto')

        # Removing M2M table for field area on 'Proyecto'
        db.delete_table('proyectos_proyecto_area')

        # Removing M2M table for field financiador on 'Proyecto'
        db.delete_table('proyectos_proyecto_financiador')


    models = {
        'proyectos.area': {
            'Meta': {'object_name': 'Area'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150', 'db_index': 'True'})
        },
        'proyectos.financiador': {
            'Meta': {'object_name': 'Financiador'},
            'enlace': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('proyectos.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150', 'db_index': 'True'})
        },
        'proyectos.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'area': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['proyectos.Area']", 'symmetrical': 'False'}),
            'estado': ('django.db.models.fields.IntegerField', [], {}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'financiador': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['proyectos.Financiador']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'monto': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'objetivos': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'resultados': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'})
        }
    }

    complete_apps = ['proyectos']
