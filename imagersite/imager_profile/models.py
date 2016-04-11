"""Models."""
from __future__ import unicode_literals
from django.conf import settings
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
    user = models.OneToOneField(
        User,
        settings.AUTH_USER_MODEL,
        related_name='profile',
    )

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









