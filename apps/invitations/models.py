from django.db import models
from django.contrib.auth import User

import datetime

class Invitation(models.Model):
    """
    Send an invitation to a user to join and activate
    their account with the site.
    
    Works with 'People'
    """
    
    inviter = models.ForeignKey(User, 
        related_name="invitations_invitation_inviter_related")
    sent = models.DateTimeField(default=datetime.datetime.now)
    invited = models.ForeignKey(User,
        related_name="invitations_invitation_invited_related")