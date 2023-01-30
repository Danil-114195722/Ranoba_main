import os
import re
import hashlib

from django.shortcuts import render
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

from .models import User


# Create your views here.

# вход
def login(request):
    data_keys = {
        'invalid_password': False,
        'user_name': None,
    }

    if request.method == 'POST':
        # переменные с данными из словаря POST
        name_or_email = request.POST.get('name_or_email')
        password = request.POST.get('password')

        try:
            # выборка экземпляра класса по введённому имени/почте
            if re.match(r'.*@.*', name_or_email):
                user = User.objects.get(email=name_or_email)
            else:
                user = User.objects.get(name=name_or_email)

            # получение соли пользователя
            salt = user.salt
            # хеширование введённого пароля
            hash_password = hashlib.pbkdf2_hmac(
                'sha256',
                password.encode('utf-8'),
                salt,
                100000
            )

            # проверка на совпадение введённого пароля
            if str(hash_password) == user.password:
                data_keys['user_name'] = user.name
            else:
                raise ObjectDoesNotExist
        except ObjectDoesNotExist:
            # Неверное имя или пароль
            data_keys['invalid_password'] = True
            return render(request, 'entrance/login.html', context=data_keys)

    return render(request, 'entrance/login.html', context=data_keys)


# регистрация
def registration(request):
    data_keys = {
        'exist_person': False,
        'all_right': False,
    }

    if request.method == 'POST':
        # переменные с данными из словаря POST
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # проверка на уникальность данных
        try:
            # хеширование пароля
            salt = os.urandom(16)
            hash_password = hashlib.pbkdf2_hmac(
                'sha256',
                password.encode('utf-8'),
                salt,
                100000
            )

            # создание экземпляра класса по введённым данным и его запись в БД
            User.objects.create(name=name, email=email, password=hash_password, salt=salt)
            data_keys['all_right'] = True
        except IntegrityError:
            # если в БД уже существует введённое имя или пароль
            data_keys['exist_person'] = True
            return render(request, 'entrance/registration.html', context=data_keys)

    return render(request, 'entrance/registration.html', context=data_keys)


# политика конфиденциальности
def politics(request):
    return render(request, 'entrance/politics.html')
