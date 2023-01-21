from django.db import models


# Create your models here.

class Authors(models.Model):
    name = models.CharField(max_length=150, null=False, unique=True)


class Genres(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)


class Books(models.Model):
    title = models.CharField(max_length=100, null=False)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, null=False)
    text = models.CharField(max_length=150, null=False, default='Пока текст отсутствует, но скоро мы его добавим')
    chapters = models.IntegerField()
    cover_picture = models.CharField(max_length=150)
    genre = models.ManyToManyField(Genres)
    likes = models.IntegerField(default=0)
