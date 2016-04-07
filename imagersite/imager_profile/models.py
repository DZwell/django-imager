"""Models."""
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class ImagerProfile(models.Model):
    """Imager Profile Model."""

    camera_model = models.CharField(max_length=200)
    photography_type = models.TextField()
    # friends = models.ManyToManyField('self')
    region = models.CharField(max_length=200)
    user = models.OneToOneField(User, unique=True, null=False)

    def is_active(self):
        """Return if the user can log in."""
        return self.user.is_active


class ActiveUserManager(models.Manager):
    """Manager to grab active users."""

    def get_query_set(self):
        """Return only active users."""
        return super(ActiveUserManager, self).get_query_set().filter(user.is_active())






