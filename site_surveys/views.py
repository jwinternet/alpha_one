#!/usr/bin/python3.12
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Site, Note
from .forms import SiteForm, NoteForm


def index(request):
    """The home page for Site Surveys."""
    return render(request, "site_surveys/index.html")


@login_required
def sites(request):
    """Show all sites."""
    sites = Site.objects.filter(owner=request.user).order_by("date_added")
    context = {"sites": sites}
    return render(request, "site_surveys/sites.html", context)


@login_required
def site(request, site_id):
    """Show a single site and all of its notes."""
    try:
        # site = Site.objects.get(id=site_id)
        site = get_object_or_404(Site, id=site_id, status=Site.Status.PUBLISHED)
        # Make sure the site belongs to the current user.
        if site.owner != request.user:
            raise Http404

        # try:
        #     site = Site.published.get(id=site_id)
        # except Site.DoesNotExist:
        #     raise Http404("Site not found")

        notes = site.note_set.order_by("-date_added")
        context = {"site": site, "notes": notes}
        return render(request, "site_surveys/site.html", context)
    except:
        return redirect("site_surveys:sites")


@login_required
def new_site(request):
    """Add a new site."""
    if request.method != "POST":
        # No data submitted; create a blank form.
        form = SiteForm()
    else:
        # POST data submitted; process data.
        form = SiteForm(data=request.POST)
        if form.is_valid():
            new_site = form.save(commit=False)
            new_site.owner = request.user
            new_site.save()
            return redirect("site_surveys:sites")

    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "site_surveys/new_site.html", context)


@login_required
def new_note(request, site_id):
    """Add a new note for a particular site."""
    site = Site.objects.get(id=site_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = NoteForm()
    else:
        # POST data submitted; process data.
        form = NoteForm(data=request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.site = site
            new_note.save()
            return redirect("site_surveys:site", site_id=site_id)

    # Display a blank or invalid form.
    context = {"site": site, "form": form}
    return render(request, "site_surveys/new_note.html", context)


@login_required
def edit_note(request, note_id):
    """Edit an existing note."""
    note = Note.objects.get(id=note_id)
    site = note.site
    if site.owner != request.user:
        raise Http404

    if request.method != "POST":
        # Initial request; pre-fill form with the current note.
        form = NoteForm(instance=note)
    else:
        # POST data submitted; process data.
        form = NoteForm(instance=note, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("site_surveys:site", site_id=site.id)

    context = {"note": note, "site": site, "form": form}
    return render(request, "site_surveys/edit_note.html", context)


# @login_required
# def note(request, note_id):
#     """Display an existing note."""
#     note = Note.objects.get(id=note_id)
#     site = note.site
#     if site.owner != request.user:
#         raise Http404
#
#     if request.method != "POST":
#         # Initial request; pre-fill form with the current note.
#         form = NoteForm(instance=note)
#     else:
#         # POST data submitted; process data.
#         form = NoteForm(instance=note, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("site_surveys:site", site_id=site.id)
#
#     context = {"note": note, "site": site, "form": form}
#     return render(request, "site_surveys/edit_note.html", context)
