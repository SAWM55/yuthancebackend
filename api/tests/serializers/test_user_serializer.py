from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.test import APITestCase
import io

from api.v1.serializers.user_serializer import UserProfileSerializer, UserSerializer
from api.models import User


class TestUserProfileSerializers(APITestCase):
    """
    Test that the UserProfileSerializers works as expected
    """

    def test_UserProfileSerializer_serializes_correctly(self):
        user_profile_data = {'username': '', 'phone_number': '',
                             'address': '', 'city': '', 'photo': None}

        serializer = UserProfileSerializer()
        content = JSONRenderer().render(serializer.data)
        stream = io.BytesIO(content)
        data = JSONParser().parse(stream)

        serializer = UserProfileSerializer(data=data)
        serializer.is_valid()

        self.assertEqual(user_profile_data, serializer.data)


class TestUserSerializers(APITestCase):
    """
    Test that the UserSerializers works as expected
    """
    user_data = {'email': '', 'first_name': '', 'last_name': '', 'password': '', 'confirm_password': '', 'profile': {
            'username': '', 'phone_number': '', 'address': '', 'city': '', 'photo': None}}

    def test_UserSerializer_serializes_correctly(self):

        serializer = UserSerializer()
        content = JSONRenderer().render(serializer.data)
        stream = io.BytesIO(content)
        data = JSONParser().parse(stream)

        serializer = UserSerializer(data=data)
        serializer.is_valid()

        user = UserSerializer()
        fields = ('url', 'email', 'first_name',
                  'last_name', 'password', 'confirm_password', 'profile')
        kwargs = {'password': {'write_only': True}}

        self.assertEqual(self.user_data, serializer.data)
        self.assertEqual(user.Meta().fields, fields)
        self.assertEqual(user.Meta().extra_kwargs, kwargs)
