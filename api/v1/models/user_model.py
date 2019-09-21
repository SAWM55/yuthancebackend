"""This module defines the user model.

Author: David Macharia
"""

from django.conf import settings
from django.db import models

class UserProfile(models.Model):
    """Adds extra user fields"""

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=9)
    address = models.CharField(max_length=255, unique=False)
    city = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='uploads', blank=True)
    