"""Choices for Users App."""

from django.db.models import TextChoices


class GenderChoices(TextChoices):

    MALE = "male", "Male"
    FEMALE = "female", "Female"
    OTHER = "other", "Other"


class RoleChoices(TextChoices):

    USER = "user", "User"
    PREMIUM = "premium", "Premium"
    ARTIST = "artist", "Artist"
    CONTENT_MANAGER = "content_manager", "Content Manager"
    MODERATOR = "moderator", "Moderator"
    ADMINISTRATOR = "administrator", "Administrator"
