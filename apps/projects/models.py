from django.contrib.auth.models import User
from django.db import models

from taggit.managers import TaggableManager

# from base.fields import FeaturedModelChoiceField
from base.models import ProjectBase, BaseType, BaseCategory, BaseTupleNode, BaseDictionaryNode
from locations.models import Location
from organisations.models import Organisation

from settings import FEATURED_COUNTRIES

class ProjectType(BaseType):
    pass
    
class ProjectCategory(BaseCategory):
    
    class Meta:
        verbose_name_plural = 'project categories'
    
class ProjectStatus(BaseTupleNode):
    
    class Meta:
        verbose_name_plural = 'project status'
        
class ProjectSiteType(BaseType):
    pass

class Project(ProjectBase):
    """
    Project
    """
    
    old_id = models.PositiveIntegerField(
        blank=True,
        null=True,
        unique=True)
    
    # Change to ManyToManyField
    project_categories = models.ManyToManyField(
        ProjectCategory,
        blank=True, 
        verbose_name="Categories",
        null=True)
    project_types = models.ManyToManyField(
        ProjectType, verbose_name="Types", 
        blank=True, null=True)
    project_status = models.ForeignKey(
        ProjectStatus, verbose_name="Status", 
        blank=True, null=True)
    
    project_website = models.URLField(
        help_text="must include http://", blank=True, null=True)
    
    client = models.CharField(
        max_length=200,
        blank=True)
    client_website = models.URLField(
        help_text="must include http://", blank=True, null=True)
    client_website_name = models.CharField(max_length=200, blank=True)
    
    number_of_stories = models.IntegerField(blank=True, null=True) 
    site_type = models.ForeignKey(
        ProjectSiteType, blank=True, null=True)
    site_size = models.FloatField(
        "Site size m3", blank=True, null=True)
    building_area = models.FloatField(
        "Building area m2", blank=True, null=True)
    budget_total = models.FloatField(
        "Budget total $", blank=True, null=True)
        
    design_documentation = models.PositiveIntegerField(
        help_text="In # months", blank=True, null=True)
        
    construction = models.PositiveIntegerField(
        help_text="In # months", blank=True, null=True)
    
    
    #Where
    street = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    suburb = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200,
        blank=True, choices=FEATURED_COUNTRIES)
    state = models.CharField(max_length=200, blank=True)
    post_code = models.CharField(max_length=10, blank=True)
    
    def consultants(self):
        """
        Gather consultants together, accross people and companies
        under one iterable
        """
        pccs = ProjectCompany.objects.filter(project=self, credit='consultant')
        pics  = ProjectIndividual.objects.filter(project=self, credit='consultant')
        
        consultants = []
        
        for c in pccs:
            consultants.append(c)
            
        for c in pics:
            consultants.append(c)
        
        return sorted(consultants, key=lambda consultant: consultant.role.name)
        
class ProjectDetail(BaseDictionaryNode):
    
    project = models.ForeignKey(Project)
    
class ProjectRoleType(BaseType):
    pass
    
class ProjectRole(models.Model):
    
    project = models.ForeignKey(
        Project)
    role = models.ForeignKey(
        ProjectRoleType,
        blank=True,
        null=True)
    
    class Meta:
        abstract = True
    
    def __unicode__(self):
        return u'%s: %s' % (self.project, self.role)
        
class ProjectCompany(ProjectRole):
    
    organisation = models.ForeignKey(
        Organisation)
    credit = models.CharField(
        "Credit type",
        blank=True, 
        choices=(
            ('project leader', 'Project leader'),
            ('consultant', 'Consultant'),
        ),
        max_length=100)
    custom_credit = models.CharField(
        "Custom credit type",
        blank=True,
        help_text="Specify a credit type not already available",
        max_length=255)
    
    class Meta:
        verbose_name_plural = 'project companies'
        
    def __unicode__(self):
        return u'%s' % (self.organisation)
        
    def content_type(self):
        return u'projectcompany'
    
class ProjectIndividual(ProjectRole):
    
    individual = models.ForeignKey(
        User,
        blank=True,
        null=True,
        verbose_name="Member/Contributor")
    credit = models.CharField(
        "Credit type",
        blank=True,
        choices=(
            ('project leader', 'Project leader'),
            ('consultant', 'Consultant'),
            ('team member', 'Team Member'),
        ),
        max_length=100)
        
    custom_credit = models.CharField(
        "Custom credit type",
        blank=True,
        help_text="Specify a credit type not already available",
        max_length=255)
            
    organisation = models.ForeignKey(
        Organisation)
        
    class Meta:
        verbose_name = 'project person'
        verbose_name_plural = 'project people'
        
    def __unicode__(self):
        try:
            return self.individual.profile_set.all()[0].display_name()
        except:
            return u'%s' % self.custom_credit
        
    def content_type(self):
        return u'projectindividual'
    
class ProjectProduct(models.Model):
    
    project = models.ForeignKey(
        Project)
    label = models.CharField(
        max_length=200)
    products = models.TextField(
        help_text="Semi-colon ';' separated list of products")
        
    def __unicode__(self):
        return u'%s' % (self.products)
    