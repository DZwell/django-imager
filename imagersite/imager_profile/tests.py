"""Tests."""
from __future__ import unicode_literals
from .models import ImagerProfile
from django.test import TestCase
from django.contrib.auth.models import User
import factory


class UserFactory(factory.django.DjangoModelFactory):
    """Set up a User factory."""

    class Meta:
        """Meta."""

        model = User

    username = 'jordan'
    email = '{}@exmaple.com'.format(username)


class SingleUserTests(TestCase):
    """Single user tests."""

    def setUp(self):
        """Single user setup."""
        self.user = UserFactory.create()
        self.user.set_password('abc')
        self.user.save()

    def test_single_user_exists(self):
        """Assert it exists."""
        self.assertTrue(self.user.profile)

    def test_active_user(self):
        """Test active user."""
        self.assertTrue(self.user.profile.is_active)


# assertTrue(self.photo in self.user.photos.all())


