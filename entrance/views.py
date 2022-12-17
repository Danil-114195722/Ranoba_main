from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'entrance/login.html')


def registration(request):
    return render(request, 'entrance/registration.html')


def politics(request):
    return render(request, 'entrance/politics.html')
