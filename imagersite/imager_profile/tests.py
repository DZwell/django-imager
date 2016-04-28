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

    username = factory.Sequence(lambda n: 'user{}'.format(n))
    email = factory.LazyAttribute(lambda a: '{}@sweet.com'.format(a.username))


class SingleUserTests(TestCase):
    """Single user tests."""

    def setUp(self):
        """Single user setup."""
        self.user = UserFactory.create()

    def test_single_user_exists(self):
        """Assert user has profile exists."""
        self.assertTrue(self.user.profile)

    def test_user_is_properly_linked(self):
        """Test."""
        self.assertTrue(self.user.profile.user, self.user.username)

    def test_active_user(self):
        """Test active user."""
        self.assertTrue(self.user.profile.is_active)


class SingleUserNotSaved(TestCase):
    """Single user created but not saved."""

    def setUp(self):
        """Setup."""
        self.user = UserFactory.build()

    def test_user_has_no_profile(self):
        """Test user has no profile before saved."""
        self.assertFalse(ImagerProfile.objects.count(), 1)


class MultiUserFriendsTests(TestCase):
    """Multiple users."""

    def setUp(self):
        """Set up multiple users."""
        self.user0 = UserFactory.create()
        self.user1 = UserFactory.create()
        self.user0.profile.friends.add(self.user1.profile)

    def test_friends(self):
        """Test friends works."""
        self.assertTrue(self.user1.profile in self.user0.profile.friends.all())

    def test_delete_works(self):
        """Test delete function works."""
        self.user1.delete()
        self.assertTrue(self.user1.profile not in self.user0.profile.friends.all())



