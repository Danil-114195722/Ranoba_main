from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'chapters', 'likes']
    list_editable = ['author', 'chapters', 'likes']
    filter_horizontal = ['genre']
    readonly_fields = ['cover_picture', 'text']
    # exclude = ['cover_picture', 'text']
    # prepopulated_fields = {'cover_picture': ('title', )}


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
