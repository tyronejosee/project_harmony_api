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
    artists = models.ManyToManyField(Artist)
    audio_file = models.FileField(upload_to="tracks/")
    track = models.PositiveIntegerField()
    duration = models.DurationField()
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    comment = models.TextField(blank=True)
    release_date = models.DateField(help_text="Release Date (Only Track)")
    rating = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    is_explicit = models.BooleanField(default=False)
    # composer

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ["pk"]
        verbose_name = "track"
        verbose_name_plural = "tracks"
