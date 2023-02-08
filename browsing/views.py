import os
from transliterate import translit

from re import split as re_split, \
    sub as re_sub
from bs4 import BeautifulSoup

from django.core.files import File
from django.shortcuts import render

from catalog import models
from Ranoba_main.settings import BASE_DIR


# Create your views here.

# страница просмотра глав
def book_review(request):
    if request.method == 'GET':
        # название книги из словаря GET
        book_title = request.GET.get('book')

    # экземпляр класса по названию книги
    one_book = models.Book.objects.get(title=book_title)
    # картинка
    image = one_book.cover_picture.url

    data = {
        'image': image,
        'one_book': one_book,
    }

    # рендерим страницу просмотра данных о книге (one_book)
    return render(request, 'browsing/review.html', context=data)


# страница для чтения глав
def read(request):
    data = {
        'chapter_error': None,
    }

    if request.method == 'GET':
        try:
            # переменные с данными из словаря GET
            name_book = request.GET.get('name_book')
            chapter = int(request.GET.get('chapter'))

        # если глава (chapter) введена не цифрой
        except ValueError:
            data['chapter_error'] = f'Вводите главу цифрами!'
            # перекидываем пользователя на 1-ю главу
            chapter = 1

    # получаем экземпляр класса по названию книги
    book = models.Book.objects.get(title=name_book)

    try:
        # берём суп файла с содержанием нужной главы
        with open(f"{str(BASE_DIR)}/{book.text}/Chapter{chapter}.html", "r") as chapter_text:
            soup = BeautifulSoup(chapter_text.read(), 'html.parser')

    # если введён неверный номер главы (chapter)
    except FileNotFoundError:
        data['chapter_error'] = 'Глава указана неверно!!!'
        chapter = 1

        # берём суп файла с содержанием 1-й главы
        with open(f"{str(BASE_DIR)}/{book.text}/Chapter{chapter}.html", "r") as chapter_text:
            soup = BeautifulSoup(chapter_text.read(), 'html.parser')

    # достаём чистый текст и название главы из файла
    book_header = soup.find('h1').text
    book_header_clean = re_split('[.:]', book_header)[-1]
    content_text = re_split('\s?<br\s?/\s?>\s?',
                            re_sub('</?[a-z0-9\s]+>', '', str(soup.find('body')).replace(book_header, '')))

    # добавляем в словарь параметры вывода
    data['book'] = book
    data['chapter'] = chapter
    data['next_chapter'] = chapter + 1
    data['previous_chapter'] = chapter - 1
    data['book_header'] = book_header_clean
    data['content_text'] = content_text

    return render(request, 'browsing/read.html', context=data)


# не сделано вообще
def listen(request, name_audio: str, chapter: int):
    # впоследствии заменить на аудио
    audio = models.Book.objects.get(title=name_audio)
    data = {
        'audio': audio,
        'chapter': chapter,
    }

    return render(request, 'browsing/listen.html', context=data)
