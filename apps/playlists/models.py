"""Models for Playlists."""

from django.conf import settings
from django.db import models
from django.db.models import UniqueConstraint

from apps.utils.models import BaseModel
from apps.tracks.models import Track

User = settings.AUTH_USER_MODEL


class Playlist(BaseModel):
    """Model definition for Playlist."""

    user_id = models.ForeignKey(
        User, related_name="playlists", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class PlaylistItem(BaseModel):
    """Model definition for PlaylistItem."""

    playlist_id = models.ForeignKey(
        Playlist,
        related_name="playlist_tracks",
        on_delete=models.CASCADE,
    )
    track_id = models.ForeignKey(
        Track,
        related_name="playlist_tracks",
        on_delete=models.CASCADE,
    )
    tags = models.JSONField(blank=True, null=True, default=list)
    order = models.PositiveIntegerField(default=0)
    is_favorite = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return str(f"{self.playlist_id} items")

    class Meta:
        ordering = ["playlist_id"]
        verbose_name = "playlist item"
        verbose_name_plural = "playlist items"
        unique_together = ("playlist", "song")
        constraints = [
            UniqueConstraint(
                fields=["playlist_id", "track_id"], name="unique_playlist_item"
            )
        ]
