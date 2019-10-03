"""This module defines the API endpoints

Author GitHub: @Dave-mash
"""

from rest_framework import routers
from django.urls import path, include
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from .v1.views.user_views import UserViewSet

schema_view = get_swagger_view(title='Pastebin API')

router = routers.DefaultRouter()  # Defines all the standard REST methods
router.register(r'users', UserViewSet)  # registers the user view

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('users', UserViewSet.as_view({'get': 'list'}), name="users"),
    url(r'^$', schema_view),
    path('', include(router.urls)),
]