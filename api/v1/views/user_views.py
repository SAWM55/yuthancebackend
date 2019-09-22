"""This module handles the user views

Author GitHub: @Dave-mash
"""

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from api.models import User
from api.v1.serializers.user_serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Defines the database objects and the serializer class"""

    queryset = User.objects.all()
    serializer_class = UserSerializer