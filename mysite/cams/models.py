from django.db import models
from django.contrib.auth.models import User


class Camera(models.Model):
    name = models.CharField(max_length=255)
    source_url = models.CharField(max_length=255)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

