from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    # image = models.ImageField(upload_to='portfolio/projects', blank=True)
    banner = models.ImageField(upload_to="portfolio/projects")
    title = models.TextField()
    description = models.TextField()
    tags = models.TextField()
    github = models.URLField()
    timestamp = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title

class ImageProject(models.Model):
    images = models.ImageField(upload_to='portfolio/projects', blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    def __str__(self):
        return self.project.title