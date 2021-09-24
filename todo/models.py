from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Task(models.Model):
    PRIORITY_LOW = 'L'
    PRIORITY_MEDIUM = 'M'
    PRIORITY_HIGH = 'H'
    PRIORITY_CHOICES = [
        (PRIORITY_LOW, 'Low'),
        (PRIORITY_MEDIUM, 'Medium'),
        (PRIORITY_HIGH, 'High'),
    ]

    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default=PRIORITY_LOW)

    def __str__(self):
        return self.name


class SubTask(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_complete = models.BooleanField(default=False)
    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
