from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "profiles"

    def __str__(self):
        return self.user.username

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    banner = models.ImageField(upload_to="portfolio/projects")
    title = models.TextField()
    description = models.TextField()
    tags = models.TextField()
    github = models.URLField()
    timestamp = models.DateField(default=timezone.now)

    class Meta:
        db_table = "projects"
        ordering = ['-timestamp']

    def __str__(self):
        return self.title

class ImageProject(models.Model):
    images = models.ImageField(upload_to='portfolio/projects', blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        db_table = "images_project"

    def __str__(self):
        return self.project.title

class Visitants(models.Model):
    visitant_ip = models.CharField(max_length=50)
    number_visits = models.IntegerField(default=0)
    black_list = models.BooleanField(default=False)

    class Meta:
        db_table = "visitants_ip"

    def __str__(self):
        return self.visitant_ip