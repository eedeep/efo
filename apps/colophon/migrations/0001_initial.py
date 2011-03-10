# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Country'
        db.create_table('colophon_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('abbrieviation', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('colophon', ['Country'])

        # Adding model 'SiteGroup'
        db.create_table('colophon_sitegroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=250, db_index=True)),
        ))
        db.send_create_signal('colophon', ['SiteGroup'])

        # Adding model 'SiteProfile'
        db.create_table('colophon_siteprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'], unique=True)),
            ('site_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['colophon.SiteGroup'], null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=250, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('abbrieviation', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['colophon.Country'], null=True, blank=True)),
        ))
        db.send_create_signal('colophon', ['SiteProfile'])

        # Adding model 'Publisher'
        db.create_table('colophon_publisher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('colophon', ['Publisher'])


    def backwards(self, orm):
        
        # Deleting model 'Country'
        db.delete_table('colophon_country')

        # Deleting model 'SiteGroup'
        db.delete_table('colophon_sitegroup')

        # Deleting model 'SiteProfile'
        db.delete_table('colophon_siteprofile')

        # Deleting model 'Publisher'
        db.delete_table('colophon_publisher')


    models = {
        'colophon.country': {
            'Meta': {'object_name': 'Country'},
            'abbrieviation': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'colophon.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'colophon.sitegroup': {
            'Meta': {'object_name': 'SiteGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'})
        },
        'colophon.siteprofile': {
            'Meta': {'object_name': 'SiteProfile'},
            'abbrieviation': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['colophon.Country']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']", 'unique': 'True'}),
            'site_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['colophon.SiteGroup']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['colophon']
