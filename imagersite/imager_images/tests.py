from __future__ import unicode_literals
from django.test import TestCase
from .models import Photo, Album, PUBLISHED_CHOICES
from imager_profile.tests import UserFactory
import random
import factory


class PhotoFactory(factory.django.DjangoModelFactory):
    """Set up a Photo factory."""

    class Meta:
        """Meta."""

        model = Photo

    title = factory.Sequence(lambda n: 'title{}'.format(n))
    description = factory.Faker('description')
    owner = factory.SubFactory(UserFactory)
    published = random.choice(PUBLISHED_CHOICES[1])
    image = factory.django.ImageField()


class AlbumFactory(factory.django.DjangoModelFactory):
    """Set up Album factory."""

    class Meta:
        """Meta."""

        model = Album

    description = factory.Faker('description')
    title = factory.Sequence(lambda n: 'title{}'.format(n))
    published = random.choice(PUBLISHED_CHOICES[1])
    owner = factory.SubFactory(UserFactory)


class SinglePhotoTest(TestCase):
    """One photo test."""

    def setUp(self):
        """Single photo setup."""
        self.photo = PhotoFactory.create()

    def test_owner(self):
        """Test owner."""
        self.assertTrue(self.)





