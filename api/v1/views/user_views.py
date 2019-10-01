"""This module handles the user views

Author GitHub: @Dave-mash
"""

from api.v1.serializers.user_serializer import UserSerializer, UserProfileSerializer
from rest_framework import viewsets
from api.v1.models.user_model import UserProfile

from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bottles to be viewed or edited.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Defines the database objects and the serializer class"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
