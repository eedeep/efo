from django import forms
from django.db.models import get_model
from base.forms import BaseAdminModelForm

class ProjectAdminModelForm(BaseAdminModelForm):
    
    class Meta:
        model = get_model('projects', 'project')
        widgets = BaseAdminModelForm.Meta.widgets

class ProjectDetailsAdminModelForm(forms.ModelForm):
    value = forms.CharField(widget=forms.Textarea(attrs={'cols':'20', 'rows':'3'}))

    class Meta:
        model = get_model('projects', 'projectdetail')
        
class ProjectProductsAdminModelForm(forms.ModelForm):
    # products = forms.CharField(widget=forms.Textarea(attrs={'cols':'20', 'rows':'3'}))

    class Meta:
        model = get_model('projects', 'projectproduct')