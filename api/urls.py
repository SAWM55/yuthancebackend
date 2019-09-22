"""This module defines the API endpoints

Author GitHub: @Dave-mash
"""

from rest_framework import routers
from django.urls import path, include

from .v1.views.user_views import UserViewSet

router = routers.DefaultRouter() # Defines all the standard REST methods
router.register(r'users', UserViewSet) # registers the user view

urlpatterns = [
    path('', include(router.urls))
]
