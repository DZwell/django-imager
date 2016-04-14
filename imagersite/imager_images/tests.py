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
    description = factory.Faker('text')
    owner = factory.SubFactory(UserFactory)
    published = random.choice(PUBLISHED_CHOICES[1])
    image = factory.django.ImageField()


class AlbumFactory(factory.django.DjangoModelFactory):
    """Set up Album factory."""

    class Meta:
        """Meta."""

        model = Album

    description = factory.Faker('text')
    title = factory.Sequence(lambda n: 'title{}'.format(n))
    published = random.choice(PUBLISHED_CHOICES[1])
    owned_by = factory.SubFactory(UserFactory)


class SinglePhotoTests(TestCase):
    """One photo test."""

    def setUp(self):
        """Single photo setup."""
        self.photo = PhotoFactory.create()

    def test_owner(self):
        """Test owner."""
        self.assertTrue(self.photo.owner)

    def test_pbulished(self):
        """Test published."""
        self.assertTrue(self.photo.published, 'private')


class PhotosInAlbumTests(TestCase):
    """Photos in album."""

    def setUp(self):
        """Photo for album."""
        self.user = UserFactory.create()
        self.photo0 = PhotoFactory.create(owner=self.user)
        self.photo1 = PhotoFactory.create()
        self.album0 = AlbumFactory.create()
        self.album1 = AlbumFactory.create()
        self.album1.photos.add(self.photo0)

    def test_no_pics_in_album(self):
        """Test empty album."""
        self.assertEqual(self.album0.photos.count(), 0)

    def test_pic_in_album(self):
        """Test photo was added to album."""
        self.assertEqual(self.album1.photos.count(), 1)

    def test_user_has_photo(self):
        """Test user has profile."""
        self.assertTrue(self.photo0.owner, self.user)

    def test_user_has_album(self):
        """Test user has album."""
        self.assertTrue(self.album1.owned_by, self.user)





