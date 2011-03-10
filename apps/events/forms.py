from django import forms
from django.db.models import get_model
from base.forms import BaseAdminModelForm

class EventAdminModelForm(BaseAdminModelForm):
    
    class Meta:
        model = get_model('events', 'event')
        widgets = BaseAdminModelForm.Meta.widgets
