from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'chapters', 'likes']


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
