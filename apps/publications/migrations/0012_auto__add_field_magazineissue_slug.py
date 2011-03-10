# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

from publications.models import MagazineIssue
from meta.utils import SlugifyUniquely

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'MagazineIssue.slug'
        db.add_column('publications_magazineissue', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=250, unique=True, null=True, db_index=True), keep_default=False)
        
        issues = MagazineIssue.objects.all()
        for issue in issues:
            if issue.issue_name:
                sluggable_string = issue.issue_name
            else:
                sluggable_string = issue.magazine
                
            issue.slug = SlugifyUniquely(sluggable_string, MagazineIssue)
            print u'Saving issue slug:: %s' % issue.slug
            issue.save()

    def backwards(self, orm):
        
        # Deleting field 'MagazineIssue.slug'
        db.delete_column('publications_magazineissue', 'slug')


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
            'Meta': {'ordering': "('_order',)", 'object_name': 'MagazineIssue'},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cover_image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'issue_month': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'issue_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'issue_number': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'issue_volume': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'issue_year': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'magazine': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['publications.Magazine']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        }
    }

    complete_apps = ['publications']
