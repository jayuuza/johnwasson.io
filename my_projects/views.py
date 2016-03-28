from my_projects.models import Project, ContentBlock, ProjectType
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404


def index(request):
    my_variables = {
        "page_project": "active",
        "nav_logo_display": "display:none;",
        "page_title": "Jonathan Wasson | Projects",
        "nav_type": "",
        "projects": Project.objects.all(),
        "types": ProjectType.objects.all(),
    }

    return render(request, 'my_projects/index.html', my_variables)

def view_project(request, slug):
    project = get_object_or_404(Project, slug=slug)

    my_variables = {
        "page_project": "active",
        "nav_logo_display": "display:none;",
        "page_title": "Jonathan Wasson | Projects",
        "nav_type": "",
        "project": project,
        "content_blocks": ContentBlock.objects.filter(parent=project),
    }

    return render(request, 'my_projects/view_project.html', my_variables)