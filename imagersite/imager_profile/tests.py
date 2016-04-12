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
        django_get_or_create = ('username',)

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    username = factory.LazyAttribute(
        lambda obj: ''.join((obj.first_name, obj.last_name)))
    password = factory.PostGenerationMethodCall('set_password', 'password')


class SingleUser(TestCase):
    """Create single user for testing."""

    def setup(self):
        """Single user setup."""
        self.user = UserFactory.create()


class SingleUserTests(SingleUser):
    """Single user tests."""

    def test_single_user_exists(self):
        """Assert it exists."""
        self.assertEqual(ImagerProfile.objects.count(), 1)

    def test_active_user(self):
        """Test active user."""
        self.assertTrue(self.user.profile.is_active)


