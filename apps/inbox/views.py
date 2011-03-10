from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

import mailchimp
from mailchimp.chimpy.chimpy import ChimpyException


from settings import MAILCHIMP_LIST_ID as list_id

def subscribe(request):
    
    
    
    list = mailchimp.utils.get_connection().get_list_by_id(list_id)
    email = request.POST.get("email-address", "")
    
    try: 

        list.subscribe(email,{'EMAIL':email})
        
    except ChimpyException:
        """
        Something happened?
        """
        import ipdb; ipdb.set_trace()
        return render_to_response(
            'inbox/fail.html',
            {
                'message': message,
            },
            context_instance=RequestContext(request))
    else:
        """
        Success!
        """
        import ipdb; ipdb.set_trace()
        return render_to_response(
            'inbox/subscribe.html',
            {
            },
            context_instance=RequestContext(request))
        
def success(request):
    
    return render_to_response(
        'inbox/success.html',
        {
            # "user": user,
        },
        context_instance=RequestContext(request))
        
def unsubscribe(request):
    
    import ipdb; ipdb.set_trace()
    
    return render_to_response(
        'inbox/unsubscribe.html',
        {
        },
        context_instance=RequestContext(request))