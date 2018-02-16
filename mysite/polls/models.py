from django.db import models
from django.utils import timezone
# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=20)
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now)


class User(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
