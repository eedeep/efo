from django import template
from django.db.models import get_model
from django.contrib.sites.models import Site
from django.contrib.comments.models import Comment

import datetime

register = template.Library()

def validate_template_tag_params(bits, arguments_count, keyword_positions):
    '''
        Raises exception if passed params (`bits`) do not match signature.
        Signature is defined by `bits_len` (acceptible number of params) and
        keyword_positions (dictionary with positions in keys and keywords in values,
        for ex. {2:'by', 4:'of', 5:'type', 7:'as'}).            
    '''    
    
    if len(bits) != arguments_count+1:
        raise template.TemplateSyntaxError("'%s' tag takes %d arguments" % (bits[0], arguments_count,))
    
    for pos in keyword_positions:
        value = keyword_positions[pos]
        if bits[pos] != value:
            raise template.TemplateSyntaxError("argument #%d to '%s' tag must be '%s'" % (pos, bits[0], value))

class MostDiscussedObjectsNode(template.Node):
    def __init__(self, context_var):
        self.context_var = context_var
        # self.limit = limit
        self.date = datetime.date.today() - datetime.timedelta(days=28)

    def render(self, context):
        # @@@ this algorithm needs work. set might be too slow?
        comments = Comment.objects.filter(submit_date__gte=self.date, site__id=Site.objects.get_current().id)
        obj_list = [comment.content_object for comment in comments]
        try:
            obj_list.sort(key=lambda obj:obj.comments_count(), reverse=True)
        except AttributeError:
            pass
        # obj_list = set(obj_list)
        # ontext[self.context_var] = obj_list[:5]
        context[self.context_var] = set(obj_list)
        return ''
        
@register.tag
def most_discussed_objects_last_month(parser, token):
    """
    Retrieves the most commented on objects in the last specified period of time.

    Example usage::

        {% most_discussed_objects_last_month as discussed_objects %} 0, 1, 2
        {% most_discussed_objects_last_month as discussed_objects limit 5 %} 0, 1, 2, 3, 4

        {% recently_added_for_model main.model_name as recent_models limit 20 %}

    """
    bits = token.contents.split()    
    validate_template_tag_params(bits, 2, {1:'as'})
    return MostDiscussedObjectsNode(bits[2])
        