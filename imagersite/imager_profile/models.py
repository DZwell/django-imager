"""Models."""
from django.db import models


# Create your models here.


class ImagerProfile(models.Model):
    """Imager Profile Model."""

    camera_model = models.CharField(max_length=200)
    photography_type = models.TextField()
    friends = models.ManyToManyField('self')
    region = models.CharField(max_length=200)



