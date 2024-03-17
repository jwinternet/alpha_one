#!/usr/bin/python3.12
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Site.Status.PUBLISHED)


class Site(models.Model):
    """A specific site location."""

    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    text = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    publish = models.DateTimeField(default=timezone.now)
    date_added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="site_surveys")
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT
    )

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    class Meta:
        ordering = ['-publish']
        verbose_name_plural = "sites"
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Note(models.Model):
    """Something specific about a site."""
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    text = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    date_added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish']
        verbose_name_plural = "notes"

    def __str__(self):
        """Return a simple string representing one or more notes."""
        return f"{self.text[:50]}..."
