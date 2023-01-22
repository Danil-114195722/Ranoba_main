from django.shortcuts import render
from .models import Book

# Create your views here.

def choice_category(request):
    all_books = Book.objects.all()

    data = {
        'all_books': all_books
    }

    return render(request, 'catalog/catalog.html', context=data)
