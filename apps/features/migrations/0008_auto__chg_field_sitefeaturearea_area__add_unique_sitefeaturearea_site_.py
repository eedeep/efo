# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'SiteFeatureArea.area'
        db.alter_column('features_sitefeaturearea', 'area', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Adding unique constraint on 'SiteFeatureArea', fields ['site', 'area']
        db.create_unique('features_sitefeaturearea', ['site_id', 'area'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'SiteFeatureArea', fields ['site', 'area']
        db.delete_unique('features_sitefeaturearea', ['site_id', 'area'])

        # Changing field 'SiteFeatureArea.area'
        db.alter_column('features_sitefeaturearea', 'area', self.gf('django.db.models.fields.CharField')(max_length=10))


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'features.feature': {
            'Meta': {'ordering': "['order']", 'object_name': 'Feature'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'default': "'article'", 'to': "orm['contenttypes.ContentType']"}),
            'feature_set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['features.FeatureSet']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'features.featureschedule': {
            'Meta': {'object_name': 'FeatureSchedule'},
            'end_date_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        'features.featureset': {
            'Meta': {'object_name': 'FeatureSet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site_feature_area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['features.SiteFeatureArea']", 'null': 'True'})
        },
        'features.sitefeaturearea': {
            'Meta': {'unique_together': "(('site', 'area'),)", 'object_name': 'SiteFeatureArea'},
            'area': ('django.db.models.fields.CharField', [], {'default': "'home'", 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']", 'null': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['features']
