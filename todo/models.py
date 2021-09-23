from django.db import models


# Create your models here.

# class User(models.Model):
#     name =


class Tasks(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    # priority
    # ok
    # created_by

# class Description(models.Model):
