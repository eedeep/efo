# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'MagazineIssue.issue_year'
        db.alter_column('publications_magazineissue', 'issue_year', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

        # Changing field 'MagazineIssue.issue_month'
        db.alter_column('publications_magazineissue', 'issue_month', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'MagazineIssue.issue_name'
        db.alter_column('publications_magazineissue', 'issue_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))


    def backwards(self, orm):
        
        # Changing field 'MagazineIssue.issue_year'
        db.alter_column('publications_magazineissue', 'issue_year', self.gf('django.db.models.fields.CharField')(default='', max_length=10))

        # Changing field 'MagazineIssue.issue_month'
        db.alter_column('publications_magazineissue', 'issue_month', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'MagazineIssue.issue_name'
        db.alter_column('publications_magazineissue', 'issue_name', self.gf('django.db.models.fields.CharField')(default='', max_length=255))


    models = {
        'publications.magazine': {
            'Meta': {'object_name': 'Magazine'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'publications.magazineissue': {
            'Meta': {'object_name': 'MagazineIssue'},
            'cover_image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'issue_month': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'issue_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'issue_number': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'issue_year': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'magazine': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['publications.Magazine']"})
        }
    }

    complete_apps = ['publications']
