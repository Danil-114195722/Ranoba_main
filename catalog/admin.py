from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'author', 'chapters', 'year', 'completeness', 'likes'
    ]
    list_editable = [
        'author', 'chapters', 'year', 'completeness', 'likes'
    ]
    filter_horizontal = ['genre']
    # readonly_fields = ['cover_picture', 'text']
    ordering = ['title']


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    list_per_page = 10


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
