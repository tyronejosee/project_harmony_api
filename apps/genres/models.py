"""Models for Genres App."""

from django.db import models

from apps.utils.models import BaseModel


class Genre(BaseModel):
    """Model definition for Genre."""

    name = models.CharField(max_length=50, unique=True)
    is_top = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ["name"]
        verbose_name = "genre"
        verbose_name_plural = "genres"
