#!/usr/bin/python3.12
from django.contrib import admin

from .models import Site, Note


admin.site.register(Site)
admin.site.register(Note)
