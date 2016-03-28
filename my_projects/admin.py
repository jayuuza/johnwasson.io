from django.contrib import admin
from my_projects.models import Project, ContentBlock, ProjectType

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Project, ProjectAdmin)
admin.site.register(ContentBlock)
admin.site.register(ProjectType)
