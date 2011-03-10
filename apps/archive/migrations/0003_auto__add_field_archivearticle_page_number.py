# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'ArchiveArticle.page_number'
        db.add_column(u'archive_article', 'page_number', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'ArchiveArticle.page_number'
        db.delete_column(u'archive_article', 'page_number')


    models = {
        'archive.archivearticle': {
            'Meta': {'object_name': 'ArchiveArticle', 'db_table': "u'archive_article'"},
            'content': ('django.db.models.fields.TextField', [], {}),
            'credit': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'introduction': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['publications.MagazineIssue']"}),
            'magazine_section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['articles.MagazineSection']"}),
            'page_number': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'review': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'type_string': ('django.db.models.fields.TextField', [], {})
        },
        'archive.archivearticlesection': {
            'Meta': {'object_name': 'ArchiveArticleSection', 'db_table': "u'archive_articlesection'"},
            'archive_article': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archive.ArchiveArticle']"}),
            'author_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'bold_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'heading': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'orig_body': ('django.db.models.fields.TextField', [], {}),
            'template': ('django.db.models.fields.IntegerField', [], {})
        },
        'archive.articlesectionimage': {
            'Meta': {'object_name': 'ArticleSectionImage'},
            'archive_article_section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archive.ArchiveArticleSection']"}),
            'caption': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'sequence': ('django.db.models.fields.IntegerField', [], {}),
            'url': ('filebrowser.fields.FileBrowseField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        },
        'articles.magazinesection': {
            'Meta': {'object_name': 'MagazineSection'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'publications.magazine': {
            'Meta': {'object_name': 'Magazine'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'show_issues': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
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
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'})
        }
    }

    complete_apps = ['archive']
