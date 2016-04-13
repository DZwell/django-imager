"""Models."""
from __future__ import unicode_literals
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible

from django.db import models


REGIONS = [
    ('pnw', 'Pacific Northwest'),
    ('ne', 'New England'),
    ('ma', 'Mid-Atlantic'),
    ('se', 'Southeast'),
    ('mw', 'Midwest'),
    ('ds', 'Deep South'),
    ('sw', 'Southwest'),
    ('cf', 'California'),
    ('ak', 'Alaska'),
    ('hi', 'Hawaii')
]


class ActiveUserManager(models.Manager):
    """convenience manager which returns only active profiles."""

    def get_queryset(self):
        """Get active managers."""
        qs = super(ActiveUserManager, self).get_queryset()
        return qs.filter(user__is_active__exact=True)


@python_2_unicode_compatible
class ImagerProfile(models.Model):
    """Imager Profile Model."""

    camera_model = models.CharField(max_length=200)
    photography_type = models.TextField()
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='friend_of')
    region = models.CharField(max_length=255, choices=REGIONS)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='profile',
    )

    objects = models.Manager()
    active = ActiveUserManager()

    @property
    def is_active(self):
        """Return all instances of active ImagerProfile."""
        return self.user.is_active

    def __str__(self):
        """Return string representation of username."""
        return self.user.username









