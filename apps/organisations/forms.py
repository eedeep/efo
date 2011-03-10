from django import forms
from django.db.models import get_model
from base.forms import BaseAdminModelForm

class OrganisationAdminModelForm(BaseAdminModelForm):
    
    class Meta:
        model = get_model('organisations', 'organisation')
        widgets = {
            'content': forms.Textarea(
                attrs={ 'class': 'mceEditor', }),
        }