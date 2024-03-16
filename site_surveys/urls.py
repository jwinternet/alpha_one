#!/usr/bin/python3.12
"""Defines URL patterns for site surveys."""
from django.urls import path

from . import views


app_name = "site_surveys"
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    # Page that shows all sites.
    path("sites/", views.sites, name="sites"),
    # Detail page for a single site.
    path("sites/<int:site_id>/", views.site, name="site"),
    # Page for adding a new site.
    path("new_site/", views.new_site, name="new_site"),
    # Page for adding a new entry.
    path("new_note/<int:site_id>/", views.new_note, name="new_note"),
    # Page for editing a note.
    path("edit_note/<int:note_id>/", views.edit_note, name="edit_note"),
]
