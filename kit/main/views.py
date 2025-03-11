from django.shortcuts import render, get_object_or_404

from .models import Page


def page_detail(request, slug) -> render:
    page = get_object_or_404(Page, slug=slug)
    return render(request, "main/page.html", {"page": page})