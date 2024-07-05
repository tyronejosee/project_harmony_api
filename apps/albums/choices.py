"""Choices for Albums App."""

from django.db import models


class MediaTypeChoices(models.TextChoices):

    SINGLE = "single", "Single"
    EP = "ep", "Ep"
    ALBUM = "album", "Album"
    COMPILATION = "compilation", "Compilation"
    SOUNDTRACK = "soundtrack", "Soundtrack"
