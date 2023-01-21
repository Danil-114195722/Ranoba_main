from django.shortcuts import render
from .models import Books

# Create your views here.

def choice_category(request):
    return render(request, 'catalog/catalog.html')
