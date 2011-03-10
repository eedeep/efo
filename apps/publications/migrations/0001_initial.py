# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Magazine'
        db.create_table('publications_magazine', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('publications', ['Magazine'])

        # Adding model 'MagazineIssue'
        db.create_table('publications_magazineissue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('magazine', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['publications.Magazine'])),
            ('issue_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('issue_number', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('issue_month', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('issue_year', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('cover_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('publications', ['MagazineIssue'])


    def backwards(self, orm):
        
        # Deleting model 'Magazine'
        db.delete_table('publications_magazine')

        # Deleting model 'MagazineIssue'
        db.delete_table('publications_magazineissue')


    models = {
        'publications.magazine': {
            'Meta': {'object_name': 'Magazine'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'publications.magazineissue': {
            'Meta': {'object_name': 'MagazineIssue'},
            'cover_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'issue_month': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'issue_number': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'issue_year': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'magazine': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['publications.Magazine']"})
        }
    }

    complete_apps = ['publications']
