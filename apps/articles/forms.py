from base.fields import UserModelMultipleChoiceField
from base.forms import BaseAdminModelForm
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import User
from django.db.models import get_model

class ArticleAdminModelForm(BaseAdminModelForm):
    publish_on_AU = forms.BooleanField(
        label="Publish on AU",
        required=False)
    publish_on_NZ = forms.BooleanField(
        label="Publish on NZ",
        required=False)

    class Meta:
        model = get_model('articles', 'article')
        widgets = BaseAdminModelForm.Meta.widgets
        widgets.update({
            'page_number': forms.TextInput(
                attrs={ 'style': 'width:35px',}
            ),
            'summary': forms.Textarea(
                attrs={ 
                        'class': 'text-counter', 
                        'maxlength': '150', 
                      }
           ),
            'introduction': forms.Textarea(
                attrs={ 
                        'class': 'text-counter', 
                        'maxlength': '115', 
                      }
           )
        })
