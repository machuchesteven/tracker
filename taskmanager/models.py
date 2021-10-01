from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    added_time = models.DateTimeField(auto_now=True, blank=True, null=True)
    start_date = models.DateField(auto_now=False, blank=True, null=True)
    deadline = models.DateField(auto_now=False, blank=True, null=True)
    status = models.CharField(max_length=16, default="UNTRACKED")
    shareholder = models.CharField(max_length=64, default="Unknown")
    description = models.TextField(blank=True, null=True)
    completed_date = models.DateTimeField(
        auto_now=False, default="", null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project', args=[str(self.id)])


class Task(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    tool_used = models.CharField(max_length=64, null=True, blank=True)
    category = models.CharField(max_length=16, default="Programming")
    added_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=16, default="PENDING")
    deadline = models.DateTimeField(auto_now=False, null=True, blank=True)
    completed_date = models.DateTimeField(
        auto_now=False, null=True, blank=True, default="")

    def __str__(self):
        return self.title

    @property
    def get_project_description(self):
        if self.project is not None:
            return self.project.description
        else:
            return f"The project is using {self.tool_used} in completeing a {self.category} task for a certain project we will find later"


class Article(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
