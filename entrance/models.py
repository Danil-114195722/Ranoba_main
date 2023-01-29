from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255, unique=True)
    salt = models.BinaryField(max_length=255)
