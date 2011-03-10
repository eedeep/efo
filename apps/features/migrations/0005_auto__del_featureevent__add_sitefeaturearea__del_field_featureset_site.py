# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'FeatureEvent'
        db.delete_table('features_featureevent')

        # Adding model 'SiteFeatureArea'
        db.create_table('features_sitefeaturearea', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'], null=True)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['features.FeatureArea'], null=True)),
        ))
        db.send_create_signal('features', ['SiteFeatureArea'])

        # Deleting field 'FeatureSet.site'
        db.delete_column('features_featureset', 'site_id')

        # Deleting field 'FeatureSet.area'
        db.delete_column('features_featureset', 'area_id')

        # Adding field 'FeatureSet.site_feature_area'
        db.add_column('features_featureset', 'site_feature_area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['features.SiteFeatureArea'], null=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'FeatureEvent'
        db.create_table('features_featureevent', (
            ('feature_set', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['features.FeatureSet'], null=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('features', ['FeatureEvent'])

        # Deleting model 'SiteFeatureArea'
        db.delete_table('features_sitefeaturearea')

        # Adding field 'FeatureSet.site'
        db.add_column('features_featureset', 'site', self.gf('django.db.models.fields.related.ForeignKey')(default=u'Home', to=orm['sites.Site']), keep_default=False)

        # Adding field 'FeatureSet.area'
        db.add_column('features_featureset', 'area', self.gf('django.db.models.fields.related.ForeignKey')(default=u'Home', to=orm['features.FeatureArea']), keep_default=False)

        # Deleting field 'FeatureSet.site_feature_area'
        db.delete_column('features_featureset', 'site_feature_area_id')


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
        'features.featurearea': {
            'Meta': {'object_name': 'FeatureArea'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
            'Meta': {'object_name': 'SiteFeatureArea'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['features.FeatureArea']", 'null': 'True'}),
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
