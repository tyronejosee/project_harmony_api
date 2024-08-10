from django.db import models

from apps.utils.models import BaseModel


class Artist(BaseModel):
    """Model definition for Artist."""

    name = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to="artists/images/",
        blank=True,
        null=True,
    )
    date_of_birth = models.DateField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)
