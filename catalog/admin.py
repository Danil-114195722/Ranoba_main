from django.contrib import admin
from django.db.models import QuerySet
from django.utils.safestring import mark_safe

from . import models


# Register your models here.

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'chapters',
        'year',
        'completeness',
        'likes',
        'update_time',
    ]
    list_editable = [
        'author',
        'year',
        'completeness',
        'likes',
    ]
    readonly_fields = [
        'preview_picture',
        'chapters',
        'text',
        'update_time',
    ]

    filter_horizontal = ['genre']
    list_filter = [
        'author',
        'genre',
        'year',
        'completeness',
    ]

    actions = ['make_complete', ]
    search_fields = ['title', ]
    ordering = ['title', ]
    list_per_page = 25


    def preview_picture(self, obj):
        return mark_safe(f'<img src="{obj.cover_picture.url}"'
                         f'style="max-height: 200px">')

    @admin.action(description='Сделать завершёнными')
    def make_complete(self, request, qset: QuerySet):
        count_updated = qset.update(
            completeness=models.Book.CPL
        )

        self.message_user(
            request,
            f'Были завершены {count_updated} книг'
        )


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name__istartswith', ]

    ordering = ['name', ]
    list_per_page = 10


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name__istartswith', ]

    ordering = ['name', ]
    list_per_page = 10
