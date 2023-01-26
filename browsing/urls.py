from django.urls import path
from . import views


urlpatterns = [
    path('read/', views.read, name='read_book'),
    path('listen/<str:name_audio>/<int:chapter>', views.listen, name='listen_audio'),
    path('book_review/', views.book_review, name='book_review'),
]
