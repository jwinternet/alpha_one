#!/usr/bin/python3.12
from django.db import models
from django.contrib.auth.models import User


class Site(models.Model):
    """A specific site location."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Note(models.Model):
    """Something specific about a site."""
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "notes"

    def __str__(self):
        """Return a simple string representing one or more notes."""
        return f"{self.text[:50]}..."
