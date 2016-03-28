from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^project/(?P<slug>[\w-]+)', views.view_project, name='project'),
]