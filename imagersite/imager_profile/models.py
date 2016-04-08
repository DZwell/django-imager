"""Models."""
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class ActiveUserManager(models.Manager):
    """Manager to grab active users."""

    def get_query_set(self):
        """Return only active users."""
        return super(ActiveUserManager, self).get_query_set().filter(user.is_active)


@python_2_unicode_compatible
class ImagerProfile(models.Model):
    """Imager Profile Model."""

    camera_model = models.CharField(max_length=200)
    photography_type = models.TextField()
    # friends = models.ManyToManyField('self')
    region = models.CharField(max_length=200)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, unique=True, null=False)

    # Need to have models.Manager since we overwrote default with ActiveUser
    # Without it, we would have lost reference to 'objects'
    objects = models.Manager()
    active = ActiveUserManager()

    @property
    def is_active(self):
        """Return all instances of active ImagerProfile."""
        return self.user.is_active

    def __str__(self):
        """Return string representation of username."""
        return self.user.username








# We control the profile, don't have code for user
# If profile is deleted, user is deleted. We want the opposite.
# How do we do that?
# Idea of Signals (pyramid also has)
# Signals hook into the listener pattern (like event listeners)
# Imager profile exists, and gets removed (handelers.py)
# first arg(sender(class that sent signal), **kwargs)
# Must ensure errors aren't raised. Log problem, do nothing.
# If errors are raised, it will prevent other things from happening
# Must put signal code into a place where Django can execute it.
# in apps.py def ready(self): from imager_profile import handlers (will register handlers)
# In init.py add default_app_config = 'imager_rofile.apps.ImagerProfileConfig'
# now Django knows about handlers
