"""This module contains tests for the user views

Author Github: @Dave-mash
"""

from api.v1.serializers.user_serializer import UserSerializer
import json
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from urllib.parse import urlsplit

User = get_user_model()


class UserViewTest(APITestCase):
    """This class contains tests for the UserView"""

    users_url = reverse("users")

    def setUp(self):
        # We want to go ahead and originally create a user.
        self.user = User.objects.create_superuser(
            email='doe@example.com', first_name='john', last_name='doe', password='password', username='johnDoe')
        self.data = {
            "email": "dave@gmail.com",
            "first_name": "",
            "last_name": "",
            "password": "password",
            "confirm_password": "password",
            "profile": {
                "username": "davemash",
                "phone_number": "254713685497",
                "address": "buru",
                "city": "Nairobi"
            }
        }

    def test_create_user(self):
        """Test that a user is able to create an account successfully"""

        response = self.client.post(self.users_url + "/?format=json", data=self.data, format='json')

        # Invalid email
        invalid_email_data = self.data.copy()
        invalid_email_data['email'] = 'dave.com'
        invalid_email_res = self.client.post(self.users_url + "/?format=json", data=invalid_email_data, format='json')

        self.assertEqual(invalid_email_res.data['email'][0], "Enter a valid email address.")
        self.assertEqual(invalid_email_res.status_code, 400)

        # Missing field
        missing_password_data = self.data.copy()
        missing_password_data2 = self.data.copy()
        del missing_password_data2['password']
        missing_password_data['password'] = ''
        
        missing_password_res = self.client.post(self.users_url + "/?format=json", data=missing_password_data, format='json')
        missing_password_res2 = self.client.post(self.users_url + "/?format=json", data=missing_password_data2, format='json')

        self.assertEqual(missing_password_res.data['password'][0], "This field may not be blank.")
        self.assertEqual(missing_password_res2.data['password'][0], "This field is required.")

        # Short password
        short_password_data = self.data.copy()
        short_password_data['password'] = 'pass'
        short_password_data['confirm_password'] = 'pass'
        short_password_res = self.client.post(
            self.users_url + "/?format=json",
            data=json.dumps(short_password_data),
            format='json'
        )

        self.assertEqual(short_password_res.status_code, 400)

        # successful registration
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['email'], self.data['email'])
        self.assertFalse('password' in response.data)

    def test_login_user(self):
        """Test that a user can log into their account"""
        
        # wrong credentials
        self.assertFalse(self.client.login(email='doe@example.com', password='pass'))
        self.assertFalse(self.client.login(email='doeexample.com', password='password'))

        # successful login
        self.assertTrue(self.client.login(email='doe@example.com', password='password'))

    def test_view_all_users(self):
        """Test that all users can be viewed"""

        # Get response data
        response = self.client.get(self.users_url)

        # Test that only authorized users can view users list
        self.assertEqual(response.status_code, 401)
        self.client.login(email='doe@example.com', password='password')
        self.assertEqual(self.client.get(self.users_url).status_code, 200)

    def test_get_single_user(self):
        """Test that a user can be fetched"""

        data = self.data.copy()
        
        new_user_response = self.client.post(self.users_url + "/?format=json", data=data, format='json')
        url = urlsplit(new_user_response.data['url'])
        user_pk = url.path.split('/')[-2]
        path = self.users_url + '/' + user_pk + '/'
        
        self.assertEqual(new_user_response.status_code, 201)
        self.assertTrue(self.client.login(email='dave@gmail.com', password='password'))

        response = self.client.get(
            path,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        """Test that a user is able to delete their account"""

        response = self.client.post(self.users_url + "/?format=json", data=self.data, format='json')
        self.assertEqual(response.status_code, 201)
        delete = self.client.delete(self.users_url + '/2/')
        del_res = self.client.get(self.users_url + '/2/')
        self.assertEqual(del_res.status_code, 404)

    def test_update_user(self):
        """Test that a user is able to update their account"""

        new_user = {
            "email": "macharia@gmail.com",
            "first_name": "",
            "last_name": "",
            "password": "password",
            "confirm_password": "password",
            "profile": {
                "username": "apipsdayv",
                "phone_number": "254729710290",
                "address": "buru",
                "city": "Nairobi"
            }
        }

        new_user_res = self.client.post(self.users_url + "/?format=json", data=self.data, format='json')
        url = urlsplit(new_user_res.data['url'])
        user_pk = url.path.split('/')[-2]
        path = self.users_url + '/' + user_pk + '/'

        self.assertEqual(new_user_res.status_code, 201)
        self.assertTrue(self.client.login(email=self.data['email'], password=self.data['password']))
        
        update_res = self.client.put(
            path,
            data=json.dumps(new_user),
            content_type='application/json'
        )

        self.assertEqual(update_res.status_code, 200)
