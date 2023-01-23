from bs4 import BeautifulSoup

from django.shortcuts import render
from catalog import models


# Create your views here.

def book_review(request, book_title: str):
    one_book = models.Book.objects.get(title=book_title)

    data = {
        'one_book': one_book,
    }
    return render(request, 'browsing/review.html', context=data)


def read(request, name_book: str, chapter: int):
    book = models.Book.objects.get(title=name_book)

    with open(f'{book.text}/Chapter{chapter}.html', 'r') as chapter_text:
        soup = BeautifulSoup(chapter_text.read(), 'html.parser')

    book_header = soup.find('h1').text
    content_text = soup.find('body').text.replace(book_header, '')

    data = {
        'book': book,
        'chapter': chapter,
        'book_header': book_header,
        'content_text': content_text,
    }
    return render(request, 'browsing/read.html', context=data)


def listen(request, name_audio: str, chapter: int):
    # впоследствии заменить на аудио
    audio = models.Book.objects.get(title=name_audio)
    data = {
        'audio': audio,
        'chapter': chapter,
    }
    return render(request, 'browsing/listen.html', context=data)
