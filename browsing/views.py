from django.shortcuts import render
from catalog import models


# Create your views here.

def show_book(request, name_book: str, chapter: int):
    book = models.Book.objects.get(title=name_book)
    data = {
        'book': book,
        'chapter': chapter,
    }
    return render(request, 'browsing/read.html', context=data)


def show_audio(request, name_audio: str, chapter: int):
    pass
#     data = {
#         'audio': name_audio,
#         'chapter': chapter,
#     }
#     return render(request, 'browsing/listen.html', context=data)

