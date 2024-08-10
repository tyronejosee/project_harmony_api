"""Models for Albums App."""

from django.db import models

from apps.utils.models import BaseModel
from apps.artists.models import Artist
from .choices import MediaTypeChoices


class Album(BaseModel):
    """Model definition for Album."""

    title = models.CharField(max_length=100)
    album_artist_id = models.ForeignKey(
        Artist,
        related_name="albums",
        on_delete=models.CASCADE,
    )
    cover = models.ImageField(
        upload_to="albums/covers/",
        # TODO: Add validators
    )
    description = models.TextField(blank=True)
    year = models.DateField()
    release_date = models.DateField()
    media_type = models.CharField(
        max_length=15,
        choices=MediaTypeChoices.choices,
    )
    total_duration = models.DurationField()
    total_tracks = models.PositiveIntegerField()
    total_dics = models.PositiveIntegerField()
    rights = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ["title"]
        verbose_name = "album"
        verbose_name_plural = "albums"
