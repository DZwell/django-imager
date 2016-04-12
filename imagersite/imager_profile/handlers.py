from __future__ import unicode_literals

from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.conf import settings
from imager_profile.models import ImagerProfile


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def confirm_profile_creation(sender, **kwargs):
    new_profile = ImagerProfile(user=kwargs['instance'])
    new_profile.save()
