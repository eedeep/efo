from django import forms
from django.db.models import get_model
from base.forms import BaseAdminModelForm

class MagazineAdminModelForm(BaseAdminModelForm):
    
    class Meta:
        model = get_model('publications', 'magazine')
        widgets = {
            'content': forms.Textarea(
                attrs={ 'class': 'mceEditor', }),
        }