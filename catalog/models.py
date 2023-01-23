from transliterate import translit
from re import sub

from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=150, null=False, unique=True)

    def __str__(self):
        return f'{self.name}'


class Genre(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    title = models.CharField(max_length=100, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=False)
    text = models.CharField(max_length=150, null=False, default='Пока текст отсутствует, но скоро мы его добавим')
    chapters = models.IntegerField()
    cover_picture = models.CharField(max_length=200)
    genre = models.ManyToManyField(Genre)
    likes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.cover_picture = sub('\s+', '_', f'Books/{translit(self.title, reversed=True)}/cover_picture/cover_picture.jpg')
        super(Book, self).save(*args, **kwargs)