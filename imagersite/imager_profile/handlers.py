from __future__ import unicode_literals

from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.conf import settings
from imager_profile.models import ImagerProfile
import logging


logger = logging.getLogger(__name__)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def confirm_profile_creation(sender, **kwargs):
    """Post save signal."""
    if kwargs.get('created', False):
        try:
            new_profile = ImagerProfile(user=kwargs['instance'])
            new_profile.save()
        except (KeyError, ValueError):
            message = 'Could not create profile for {}'
            logger.error(message.format(kwargs['instance']))


# @receiver(pre_delete, sender=settings.AUTH_USER_MODEL)
# def delete_imager_profile(sender, **kwargs):
#     """Pre delete signal."""
#     try:
#         kwargs['instance'].profile.delete()
#     except ()


