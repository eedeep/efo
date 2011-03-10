from django.contrib import admin
from django.db.models import get_model

import legacy.models as models

# import ipdb; ipdb.set_trace()

# for k, v in models.__dict__: 
#     try:
#         admin.site.register(v)
#     except:
#         pass

admin.site.register(get_model('legacy', 'eventsevent'))
admin.site.register(get_model('legacy', 'eventseventtype'))
