"""This module defines all models for Yuthancebackend.

Author: David Macharia
"""
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    """Extends Django's AbstractUser model"""
    pass
    username = models.CharField(blank=True, null=True, max_length=50)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):
    """Adds extra user fields"""
    pass
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    # phone_number = models.CharField(min_length=9)
    address = models.CharField(max_length=255, unique=False)
    city = models.CharField(max_length=50)