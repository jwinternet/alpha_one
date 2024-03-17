#!/usr/bin/python3.12
from django import forms

from .models import Site, Note


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ["text"]
        labels = {"text": ""}


# class NoteForm(forms.ModelForm):
#     class Meta:
#         model = Note
#         fields = ["text"]
#         labels = {"text": ""}
#         widgets = {"text": forms.Textarea(attrs={"cols": 80})}


class NoteForm(forms.ModelForm):
    title = forms.CharField(max_length=255,)
    content = forms.CharField(widget=forms.Textarea(),)
    is_published = forms.BooleanField(required=False,)
    class Meta:
        model = Note
        fields = ["text"]
        labels = {"text": ""}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
