import os
from re import sub
from transliterate import translit

from django.db import models
from django.core.validators import MinValueValidator


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
    CPL = 'Завершено'
    INC = 'Не завершено'
    COMPLETENESS_CHOICES = [
        (CPL, 'Завершено'),
        (INC, 'Не завершено')]

    title = models.CharField(max_length=100, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=False)
    text = models.CharField(max_length=150, null=False)
    chapters = models.IntegerField(validators=(MinValueValidator(0), ))
    year = models.IntegerField(null=True, blank=True)
    completeness = models.CharField(max_length=12, choices=COMPLETENESS_CHOICES, default=INC)
    cover_picture = models.CharField(max_length=200)
    genre = models.ManyToManyField(Genre)
    likes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.translit_title = sub('\s+', '_', translit(self.title, reversed=True))

        self.cover_picture = f'{self.translit_title}/cover_picture/cover_picture.jpg'
        self.text = f'Books/{self.translit_title}/text'

        try:
            os.makedirs(f"{os.getcwd()}/Books/{self.translit_title}/cover_picture")
            os.mkdir(f"{os.getcwd()}/Books/{self.translit_title}/text")
        except:
            print('Such directory already exists')

        super(Book, self).save(*args, **kwargs)


