from django.http import HttpResponse
from django.shortcuts import render
import urllib, hashlib
from my_projects.models import Project

# Create your views here.
def index(request):
    email = "wassonjonathan@gmail.com"
    default = ""
    size = 300

    # construct the url
    gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
    my_variables = {
        "page_home": "active",
        "nav_type": "transparent-nav",
        "page_title": "Jonathan Wasson | Software Developer",
        "nav_logo_display": "",
        "projects": Project.objects.all(),
        "gravatar_url": gravatar_url
    }

    return render(request, 'home/index.html', my_variables)

def health(request):
    return HttpResponse("OK")