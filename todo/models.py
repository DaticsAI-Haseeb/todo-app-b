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



# class Tasks(models.Model):
#     name = models.CharField(max_length=255)
#     date_created = models.DateTimeField(auto_now_add=True)
#     last_update = models.DateTimeField(auto_now=True)
    # priority
    # ok
    # created_by

# class Description(models.Model):
