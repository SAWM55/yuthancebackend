"""This module defines the API endpoints

Author GitHub: @Dave-mash
"""

from rest_framework import routers
from django.urls import path, include
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .v1.views.user_views import UserViewSet


router = routers.DefaultRouter()  # Defines all the standard REST methods
router.register(r'users', UserViewSet)  # registers the user view

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('users', UserViewSet.as_view({'get': 'list'}), name="users"),
    path('', include(router.urls)),
]