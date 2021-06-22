from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Data(models.Model):
    name = models.CharField(max_length=256)
    contact = models.IntegerField()
    hobbies = models.CharField(max_length=256)

    def __str__(self):
        return self.name