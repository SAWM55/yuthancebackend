"""This module handles the user views

Author GitHub: @Dave-mash
"""

from api.v1.serializers.user_serializer import UserSerializer, UserProfileSerializer
from rest_framework import viewsets
from api.v1.models.user_model import UserProfile
from rest_framework.permissions import AllowAny
from api.permissions import IsLoggedInUserOrAdmin, IsAdminUser

from django.contrib.auth import get_user_model

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """Defines the database objects and the serializer class"""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """permission restrictions"""
        
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
