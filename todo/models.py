from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Tasks(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # priority
    PRIORITY_LOW = 'L'
    PRIORITY_MEDIUM = 'M'
    PRIORITY_HIGH = 'H'
    PRIORITY_CHOICES = [
        (PRIORITY_LOW, 'Low'),
        (PRIORITY_MEDIUM, 'Medium'),
        (PRIORITY_HIGH, 'High'),
    ]
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default=PRIORITY_LOW)

    def __str__(self):
        return self.name


class Description(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
