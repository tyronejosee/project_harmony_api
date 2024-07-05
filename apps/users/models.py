"""Models for Users App."""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from apps.utils.models import BaseModel
from .managers import UserManager
from .choices import RoleChoices


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    """Model definition for User."""

    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to="users/", blank=True)
    country = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    role = models.CharField(
        max_length=25,
        choices=RoleChoices.choices,
        default=RoleChoices.USER,
    )
    is_active = models.BooleanField(default=True)
    is_premium = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        ordering = ["pk"]
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return str(self.username)
