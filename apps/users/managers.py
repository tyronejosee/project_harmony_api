"""Managers for Users App."""

from django.contrib.auth.models import BaseUserManager

from .choices import RoleChoices


class UserManager(BaseUserManager):
    """Manager for User model."""

    def create_user(self, email, password=None, **kwargs):
        """Creates a user with the given email and password."""
        if not email:
            raise ValueError("Users must have an email address.")

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        """Creates a superuser with the given email and password."""
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("role", RoleChoices.ADMINISTRATOR)

        if kwargs.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if kwargs.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        user = self.create_user(email, password=password, **kwargs)
        return user
