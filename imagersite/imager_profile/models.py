"""Models."""
from django.db import models


# Create your models here.


class ImagerProfile(models.Model):
    """Imager Profile Model."""

    camera_model = models.CharField(max_length=200)
    photography_type = models.TextField()
    Friends = models.ManyToManyField('self')
    Region = models.CharField(max_length=200)



