from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink

# Create your models here.
class ProjectType(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return '%s' % self.title

class Project(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    image = models.ImageField(upload_to='john_wasson/static')
    type = models.ForeignKey(ProjectType)

    slug = models.SlugField(max_length=100, unique=True)
    enabled = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_project_details', None, { 'slug': self.slug })

class ContentBlock(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    image = models.ImageField(upload_to='john_wasson/static')
    parent = models.ForeignKey(Project)

    def __unicode__(self):
        return '%s' % self.title
