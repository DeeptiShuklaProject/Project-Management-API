from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_projects')  # Add related_name here
    created_at = models.DateTimeField(auto_now_add=True)

class ProjectMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='members')  # Add related_name here
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_memberships')  # Add related_name here
    role = models.CharField(max_length=50)

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_tasks')  # Add related_name here
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')  # Add related_name here
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')  # Add related_name here
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')  # Add related_name here
    created_at = models.DateTimeField(auto_now_add=True)
