import os
from re import sub
from transliterate import translit

from django.db import models
from django.core.validators import MinValueValidator
from django.utils.timezone import now


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
    description = models.TextField()

    text = models.CharField(max_length=150, null=False)
    chapters = models.IntegerField(validators=(
        MinValueValidator(0),
    ))
    update_time = models.DateTimeField(default=now)

    year = models.IntegerField(null=True, blank=True)
    completeness = models.CharField(max_length=12, choices=COMPLETENESS_CHOICES, default=INC)

    genre = models.ManyToManyField(Genre)
    likes = models.IntegerField(default=0, validators=(
        MinValueValidator(0),
    ))
    cover_picture = models.ImageField(default='', upload_to='cover_picture')

    def save(self, *args, **kwargs):
        # транслитим название книги
        self.translit_title = sub('\s+', '_', translit(self.title, reversed=True))

        try:
            # создаём каталог для хранения глав
            os.mkdir(f"{os.getcwd()}/Books/{self.translit_title}/text")

            # создаём путь к хранящимся главам
            self.text = f'Books/{self.translit_title}/text'
        # если запись уже была создана, а сейчас только обновилась
        except:
            print('Such directory already exists')

        # обновляем время обновления записи в бд
        self.update_time = now()
        # автоматически проставляем (обновляем) кол-во глав
        self.chapters = len(os.listdir(os.getcwd() + '/' + self.text))

        # запускаем метод save для сохранения изменений
        super(Book, self).save(*args, **kwargs)


