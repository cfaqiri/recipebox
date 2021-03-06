from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return f"{self.title} saved by {self.user}"


