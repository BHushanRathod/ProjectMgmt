import datetime

from django.db import models
from django.contrib.auth.models import User as UserModel

# Create your models here.
from django.urls import reverse


def nameFile(instance, filename):
    print("nameFIle: ", instance, filename)
    return '/'.join(['images', str(filename), filename])


class Projects(models.Model):
    title = models.CharField(max_length=50)
    creator = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='created_project')
    desc = models.TextField(default="", max_length=1024, blank=True)
    duration = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to=nameFile, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)
    is_active = models.BooleanField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Project"


class Task(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(default="", max_length=1024, blank=True)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('PLAN', 'Planned'),
        ('PROG', 'In Progress'),
        ('COMP', 'Completed')
    )
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default='PLAN')
    creator = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='created_tasks')
    assignee = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    planned_date = models.DateField(auto_now_add=True)
    accepted_date = models.DateField(null=True, blank=True)
    completed_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=1)

    def __str__(self):
        return self.title


class SubTask(models.Model):
    subtitle = models.CharField(max_length=100)
    desc = models.TextField(default="", max_length=1024, blank=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=1)

    def __str__(self):
        return self.subtitle