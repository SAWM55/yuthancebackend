"""This module defines the user serializer classes.

Author GitHub: @Dave-mash
"""

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

from api.v1.models.user_model import UserProfile
from ...models import User


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes userProfile as part of the User model"""

    class Meta:
        model = UserProfile
        fields = ('phone_number', 'address', 'city', 'photo')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes the User model and nests the UserProfile model"""

    profile = UserProfileSerializer(required=True)
    url = serializers.HyperlinkedIdentityField(view_name="user-detail")

    class Meta:

        model = User
        fields = ('url', 'email', 'first_name',
                  'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Create and return a new User instance, given the validated data
        """

        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password) # password hashing
        user.save()
        UserProfile.objects.create(user=user, **profile_data)

        return user

    def update(self, instance, validated_data):
        """
        Update and return existing User instance, given the validated data
        """
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.phone_number = profile_data.get(
            'phone_number', profile.phone_number)
        profile.address = profile_data.get('address', profile.address)
        profile.city = profile_data.get('city', profile.city)
        profile.photo = profile_data.get('photo', profile.photo)
        profile.save()

        return instance
