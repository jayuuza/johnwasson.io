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
    image = models.ImageField(upload_to='my_projects')
    type = models.ForeignKey(ProjectType)

    slug = models.SlugField(max_length=100, unique=True)
    enabled = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s' % self.title

class ContentBlock(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    image = models.ImageField(upload_to='my_projects')
    parent = models.ForeignKey(Project)

    def __unicode__(self):
        return '%s' % self.title
