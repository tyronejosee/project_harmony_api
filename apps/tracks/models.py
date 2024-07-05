"""Models for Tracks Apps."""

from django.db import models

from apps.utils.models import BaseModel
from apps.artists.models import Artist
from apps.albums.models import Album
from apps.genres.models import Genre


class Track(BaseModel):
    """Model definition for Track."""

    title = models.CharField(max_length=255)
    album_id = models.ForeignKey(
        Album,
        related_name="tracks",
        on_delete=models.CASCADE,
    )
    artist_id = models.ForeignKey(
        Artist,
        related_name="tracks",
        on_delete=models.CASCADE,
    )
    duration = models.DurationField()
    audio_file = models.FileField(upload_to="tracks/")
    genres = models.ManyToManyField(Genre, related_name="tracks")
    is_explicit_content = models.BooleanField(default=False)
    track = models.PositiveIntegerField()
    rating = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    # composer
    # play_count

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ["pk"]
        verbose_name = "track"
        verbose_name_plural = "tracks"
