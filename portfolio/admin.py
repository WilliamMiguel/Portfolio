from django.contrib import admin
from portfolio.models import Profile, Project, ImageProject,  Visitants

# Register your models here.
class ImageProjectAdmin(admin.TabularInline):
    model = ImageProject

class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ImageProjectAdmin
    ]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Profile)
admin.site.register(ImageProject)
admin.site.register(Visitants)


