# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ProjectType'
        db.create_table('projects_projecttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
        ))
        db.send_create_signal('projects', ['ProjectType'])

        # Adding model 'ProjectCategory'
        db.create_table('projects_projectcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
        ))
        db.send_create_signal('projects', ['ProjectCategory'])

        # Adding model 'ProjectStatus'
        db.create_table('projects_projectstatus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('display', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('projects', ['ProjectStatus'])

        # Adding model 'ProjectSiteType'
        db.create_table('projects_projectsitetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
        ))
        db.send_create_signal('projects', ['ProjectSiteType'])

        # Adding model 'Project'
        db.create_table('projects_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('summary', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='projects_project_created_by', null=True, to=orm['auth.User'])),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='projects_project_modified_by', null=True, to=orm['auth.User'])),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('published', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('published_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='projects_project_published_by', null=True, to=orm['auth.User'])),
            ('project_status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.ProjectStatus'], null=True, blank=True)),
            ('client', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('client_website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('client_website_name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('number_of_stories', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('site_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.ProjectSiteType'], null=True, blank=True)),
            ('site_size', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('building_area', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('budget_total', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('design_documentation', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('construction', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('suburb', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('post_code', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
        ))
        db.send_create_signal('projects', ['Project'])

        # Adding M2M table for field sites on 'Project'
        db.create_table('projects_project_sites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['projects.project'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique('projects_project_sites', ['project_id', 'site_id'])

        # Adding M2M table for field tags on 'Project'
        db.create_table('projects_project_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['projects.project'], null=False)),
            ('tag', models.ForeignKey(orm['taggit.tag'], null=False))
        ))
        db.create_unique('projects_project_tags', ['project_id', 'tag_id'])

        # Adding M2M table for field project_categories on 'Project'
        db.create_table('projects_project_project_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['projects.project'], null=False)),
            ('projectcategory', models.ForeignKey(orm['projects.projectcategory'], null=False))
        ))
        db.create_unique('projects_project_project_categories', ['project_id', 'projectcategory_id'])

        # Adding M2M table for field project_types on 'Project'
        db.create_table('projects_project_project_types', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['projects.project'], null=False)),
            ('projecttype', models.ForeignKey(orm['projects.projecttype'], null=False))
        ))
        db.create_unique('projects_project_project_types', ['project_id', 'projecttype_id'])

        # Adding model 'ProjectDetail'
        db.create_table('projects_projectdetail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('value', self.gf('django.db.models.fields.TextField')()),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Project'])),
        ))
        db.send_create_signal('projects', ['ProjectDetail'])

        # Adding model 'ProjectCompany'
        db.create_table('projects_projectcompany', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Project'])),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('organisation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['organisations.Organisation'])),
            ('credit', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('projects', ['ProjectCompany'])

        # Adding model 'ProjectIndividual'
        db.create_table('projects_projectindividual', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Project'])),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('individual', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('credit', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('organisation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['organisations.Organisation'])),
        ))
        db.send_create_signal('projects', ['ProjectIndividual'])

        # Adding model 'ProjectProduct'
        db.create_table('projects_projectproduct', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Project'])),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('products', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('projects', ['ProjectProduct'])


    def backwards(self, orm):
        
        # Deleting model 'ProjectType'
        db.delete_table('projects_projecttype')

        # Deleting model 'ProjectCategory'
        db.delete_table('projects_projectcategory')

        # Deleting model 'ProjectStatus'
        db.delete_table('projects_projectstatus')

        # Deleting model 'ProjectSiteType'
        db.delete_table('projects_projectsitetype')

        # Deleting model 'Project'
        db.delete_table('projects_project')

        # Removing M2M table for field sites on 'Project'
        db.delete_table('projects_project_sites')

        # Removing M2M table for field tags on 'Project'
        db.delete_table('projects_project_tags')

        # Removing M2M table for field project_categories on 'Project'
        db.delete_table('projects_project_project_categories')

        # Removing M2M table for field project_types on 'Project'
        db.delete_table('projects_project_project_types')

        # Deleting model 'ProjectDetail'
        db.delete_table('projects_projectdetail')

        # Deleting model 'ProjectCompany'
        db.delete_table('projects_projectcompany')

        # Deleting model 'ProjectIndividual'
        db.delete_table('projects_projectindividual')

        # Deleting model 'ProjectProduct'
        db.delete_table('projects_projectproduct')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'features.feature': {
            'Meta': {'object_name': 'Feature'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'ordering': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'organisations.organisation': {
            'Meta': {'object_name': 'Organisation'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'organisations_organisation_created_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'feature': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'logo_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'organisations_organisation_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'organisation_expertise': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['organisations.OrganisationExpertise']", 'null': 'True', 'blank': 'True'}),
            'organisation_type': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['organisations.OrganisationType']", 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'post_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'published_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'organisations_organisation_published_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sites.Site']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'organisations_organisation_tags'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['taggit.Tag']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'website_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'organisations.organisationexpertise': {
            'Meta': {'object_name': 'OrganisationExpertise'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'organisations.organisationtype': {
            'Meta': {'object_name': 'OrganisationType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'projects.project': {
            'Meta': {'object_name': 'Project'},
            'budget_total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'building_area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'client': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'client_website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'client_website_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'construction': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'projects_project_created_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'design_documentation': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'projects_project_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'number_of_stories': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'post_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'project_categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['projects.ProjectCategory']", 'null': 'True', 'blank': 'True'}),
            'project_status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.ProjectStatus']", 'null': 'True', 'blank': 'True'}),
            'project_types': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['projects.ProjectType']", 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'published_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'projects_project_published_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'site_size': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'site_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.ProjectSiteType']", 'null': 'True', 'blank': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sites.Site']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'projects_project_tags'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['taggit.Tag']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'projects.projectcategory': {
            'Meta': {'object_name': 'ProjectCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'projects.projectcompany': {
            'Meta': {'object_name': 'ProjectCompany'},
            'credit': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['organisations.Organisation']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']"}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'projects.projectdetail': {
            'Meta': {'object_name': 'ProjectDetail'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']"}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        'projects.projectindividual': {
            'Meta': {'object_name': 'ProjectIndividual'},
            'credit': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'individual': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['organisations.Organisation']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']"}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'projects.projectproduct': {
            'Meta': {'object_name': 'ProjectProduct'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'products': ('django.db.models.fields.TextField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']"})
        },
        'projects.projectsitetype': {
            'Meta': {'object_name': 'ProjectSiteType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'projects.projectstatus': {
            'Meta': {'object_name': 'ProjectStatus'},
            'display': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'projects.projecttype': {
            'Meta': {'object_name': 'ProjectType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'})
        }
    }

    complete_apps = ['projects']
