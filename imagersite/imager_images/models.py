from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible


PUBLISHED_CHOICES = (('private', 'private'), ('public', 'public'), ('shared', 'shared'))
PUBLISHED_DEFAULT = PUBLISHED_CHOICES[0]


@python_2_unicode_compatible
class Photo(models.Model):
    """Photo class."""

    image = models.ImageField(upload_to='media')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='photos')
    title = models.CharField(max_length=250)
    description = models.TextField()
    uploaded = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    album = models.ManyToManyField('Album', related_name='album')
    published = models.CharField(
        max_length=10,
        choices=PUBLISHED_CHOICES
    )

    def __str__(self):
        """Return title."""
        return str(self.title)


@python_2_unicode_compatible
class Album(models.Model):
    """Album class."""

    photos = models.ManyToManyField('Photo', related_name='photos')
    owned_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='albums')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    cover_photo = models.ForeignKey('Photo', related_name='cover')
    published = models.CharField(
        max_length=10,
        choices=PUBLISHED_CHOICES,
        default=PUBLISHED_DEFAULT
    )

    def __str__(self):
        """Return title."""
        return str(self.title)

