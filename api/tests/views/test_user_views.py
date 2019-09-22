"""This module contains tests for the user views

Author Github: @Dave-mash
"""

from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status


class AccountsTest(APITestCase):
    # def setUp(self):
    #     # We want to go ahead and originally create a user.
    #     self.test_user = User.objects.create_user(
    #         'john@example.com',
    #         'John',
    #         'Doe',
    #         'testpassword'
    #     )

    #     # URL for creating an account.
    #     self.create_url = reverse('register')

    def test_view_all_users(self):
        """Test that all users can be viewed"""
        


    def test_create_user(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        pass
        # data = {
        #     'first_name': 'Jane',
        #     'last_name': 'Doe',
        #     'email': 'jane@example.com',
        #     'password': 'somepassword'
        # }

        # response = self.client.post(self.create_url, data, format='json')

        # # We want to make sure we have two users in the database..
        # self.assertEqual(User.objects.count(), 2)
        # # And that we're returning a 201 created code.
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # # Additionally, we want to return the username and email upon successful creation.
        # self.assertEqual(response.data['username'], data['username'])
        # self.assertEqual(response.data['email'], data['email'])
        # self.assertFalse('password' in response.data)
