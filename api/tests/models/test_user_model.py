"""This module contains tests for the user model

Author GitHub: @Dave-mash
"""
from django.test import TestCase
from ...models import User


class TestUserModel(TestCase):

    def setUp(self):
        user = User.objects.create(email='doe@example.com')

    def test_user_model(self):

        fields = ['username', 'first_name', 'last_name']

        user = User.objects.get(email='doe@example.com')
        self.assertEqual(user.get_user_by_email(), 'doe@example.com')
        self.assertEqual(user.__str__(), 'doe@example.com')
        self.assertEqual(user.REQUIRED_FIELDS, fields)
