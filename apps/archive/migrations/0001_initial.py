# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ArchiveArticle'
        db.create_table(u'archive_article', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('magazine_section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['articles.MagazineSection'])),
            ('introduction', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('issue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['publications.MagazineIssue'])),
            ('credit', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('review', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('type_string', self.gf('django.db.models.fields.TextField')()),
            ('summary', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('archive', ['ArchiveArticle'])

        # Adding model 'ArchiveArticleSection'
        db.create_table(u'archive_articlesection', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('archive_article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archive.ArchiveArticle'])),
            ('heading', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('bold_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('author_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('orig_body', self.gf('django.db.models.fields.TextField')()),
            ('template', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('archive', ['ArchiveArticleSection'])

        # Adding model 'ArticleSectionImage'
        db.create_table('archive_articlesectionimage', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('archive_article_section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archive.ArchiveArticleSection'])),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('sequence', self.gf('django.db.models.fields.IntegerField')()),
            ('caption', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('archive', ['ArticleSectionImage'])


    def backwards(self, orm):
        
        # Deleting model 'ArchiveArticle'
        db.delete_table(u'archive_article')

        # Deleting model 'ArchiveArticleSection'
        db.delete_table(u'archive_articlesection')

        # Deleting model 'ArticleSectionImage'
        db.delete_table('archive_articlesectionimage')


    models = {
        'archive.archivearticle': {
            'Meta': {'object_name': 'ArchiveArticle', 'db_table': "u'archive_article'"},
            'content': ('django.db.models.fields.TextField', [], {}),
            'credit': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'introduction': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['publications.MagazineIssue']"}),
            'magazine_section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['articles.MagazineSection']"}),
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
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
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
