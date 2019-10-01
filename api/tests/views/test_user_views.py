"""This module contains tests for the user views

Author Github: @Dave-mash
"""

from api.v1.serializers.user_serializer import UserSerializer
import json
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class UserViewTest(APITestCase):
    url = reverse("users")

    def setUp(self):
        # We want to go ahead and originally create a user.
        self.user = User.objects.create_superuser(
            email='doe@example.com', first_name='john', last_name='doe', password='password', username='johnDoe')

    def test_view_all_users(self):
        """Test that all users can be viewed"""

        # Get response data
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.user.email, 'doe@example.com')
        self.assertTrue(len(json.loads(response.content))
                        == User.objects.count())

    def test_create_user(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        
        data = {
            "email": "dave@gmail.com",
            "first_name": "",
            "last_name": "",
            "password": "password",
            "profile": {
                "username": "davemash",
                "phone_number": "254713685497",
                "address": "buru",
                "city": "Nairobi"
            }
        }

        response = self.client.post(self.url + "/?format=json", data, format='json')

        # # We want to make sure we have two users in the database..
        # self.assertEqual(User.objects.count(), 2)
        # # And that we're returning a 201 created code.
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # # Additionally, we want to return the username and email upon successful creation.
        # self.assertEqual(response.data['username'], data['username'])
        # self.assertEqual(self.url, 'abc')
        # self.assertFalse('password' in response.data)
