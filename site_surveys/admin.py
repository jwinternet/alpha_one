#!/usr/bin/python3.12
from django.contrib import admin

from .models import Site, Note


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ("text", "slug", "owner", "publish", "status")
    list_filter = ["status", "date_added", "publish", "owner"]
    search_fields = ["text"]
    prepopulated_fields = {"slug": ("text",)}
    raw_id_fields = ["owner"]
    date_hierarchy = "publish"
    ordering = ["status", "publish"]


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("site", "slug", "text", "publish")
