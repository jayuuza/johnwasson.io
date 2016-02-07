from datetime import timedelta
from django.shortcuts import render
from django.utils import timezone


def index(request):
    my_variables = {
        "page_blog": "active",
        "page_title": "Jonathan Wasson | Blog",
        "tug": timezone.now() + timedelta(days=1)
    }

    return render(request, 'blog/index.html', my_variables)
