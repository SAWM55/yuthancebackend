from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.test import APITestCase
import io

from api.v1.serializers.user_serializer import UserProfileSerializer, UserSerializer
from api.models import User


class TestUserSerializers(APITestCase):
    """
    Test that the UserProfileSerializers works as expected
    """

    def test_UserSerializer_serializes_correctly(self):
        user_data = {'email': '', 'first_name': '', 'last_name': '', 'password': '', 'profile': {
            'phone_number': '', 'address': '', 'city': '', 'photo': None}}

        serializer = UserSerializer()
        content = JSONRenderer().render(serializer.data)
        stream = io.BytesIO(content)
        data = JSONParser().parse(stream)

        serializer = UserSerializer(data=data)
        serializer.is_valid()

        self.assertEqual(user_data, serializer.data)

    def test_UserProfileSerializer_serializes_correctly(self):
        user_profile_data = {'phone_number': '',
                        'address': '', 'city': '', 'photo': None}

        serializer = UserProfileSerializer()
        content = JSONRenderer().render(serializer.data)
        stream = io.BytesIO(content)
        data = JSONParser().parse(stream)

        serializer = UserProfileSerializer(data=data)
        serializer.is_valid()

        self.assertEqual(user_profile_data, serializer.data)
