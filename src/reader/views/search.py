
from django.db.models import Q
from django.shortcuts import render

from reader.models import ParsedImages


def search_view(request):

    parsed_images = ParsedImages.objects.all()

    return render(request, "search/search.html", {
        'parsed_images': parsed_images,
    })


def search(request):

    search_text = request.POST.get('search', None)

    if search_text:
        search_text = search_text.lower()
        or_lookup = Q(text__icontains=search_text)
        parsed_images = ParsedImages.objects.filter(or_lookup)
    else:
        parsed_images = ParsedImages.objects.all()

    return render(request, "search/search_result.html", {
        'parsed_images': parsed_images,
    })
