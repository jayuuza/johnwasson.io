from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    my_variables = {
        "page_title": "TUG HOME"
    }

    return render(request, 'home/index.html', my_variables)
