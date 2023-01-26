from re import split as re_split
from re import sub as re_sub
from re import compile as re_compile
from bs4 import BeautifulSoup

from django.shortcuts import render
from catalog import models


# Create your views here.

def book_review(request):
    if request.method == 'GET':
        book_title = request.GET.get('book')

    one_book = models.Book.objects.get(title=book_title)

    data = {
        'one_book': one_book,
    }
    return render(request, 'browsing/review.html', context=data)


def read(request):
    if request.method == 'GET':
        name_book = request.GET.get('name_book')
        chapter = int(request.GET.get('chapter'))

    book = models.Book.objects.get(title=name_book)

    with open(f"{book.text}/Chapter{chapter}.html", "r") as chapter_text:
        soup = BeautifulSoup(chapter_text.read(), 'html.parser')

    book_header = soup.find('h1').text
    book_header_clean = re_split('[.:]', book_header)[-1]
    content_text = re_split('\s?<br\s?/\s?>\s?',
                                      re_sub('</?[a-z0-9\s]+>', '',str(soup.find('body')).replace(book_header, '')))

    data = {
        'book': book,
        'chapter': chapter,
        'next_chapter': chapter + 1,
        'previous_chapter': chapter - 1,
        'book_header': book_header_clean,
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
