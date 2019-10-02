"""
This module defines user permissions
"""

from rest_framework import permissions


class IsLoggedInUserOrAdmin(permissions.BasePermission):
    """permission of accessing a specific object"""

    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff


class IsAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        """permission flag on a general level"""

        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        """permission of accessing a specific object"""

        return request.user and request.user.is_staff
