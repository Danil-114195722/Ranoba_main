from django.urls import path
from . import views


urlpatterns = [
    path('read/<str:name_book>/<int:chapter>', views.show_book, name='show_book'),
    path('listen/<str:name_audio>/<int:chapter>', views.show_audio, name='show_audio'),
]
