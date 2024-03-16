#!/usr/bin/python3.12
from django import forms

from .models import Site, Note


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ["text"]
        labels = {"text": ""}


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["text"]
        labels = {"text": ""}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
