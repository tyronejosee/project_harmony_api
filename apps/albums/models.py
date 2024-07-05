"""Models for Albums App."""

from django.db import models

from apps.utils.models import BaseModel
from apps.artists.models import Artist
from .choices import MediaTypeChoices


class Album(BaseModel):
    """Model definition for Album."""

    title = models.CharField(max_length=100)
    Album_artist_id = models.ForeignKey(
        Artist,
        related_name="albums",
        on_delete=models.CASCADE,
    )
    purchase_date = models.DateField()
    cover = models.ImageField(
        upload_to="albums/covers/",
        # TODO: Add validators
    )
    media_type = models.CharField(
        max_length=15,
        choices=MediaTypeChoices.choices,
        default=MediaTypeChoices.ALBUM,
    )
    xid = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        verbose_name = "album"
        verbose_name_plural = "albums"
