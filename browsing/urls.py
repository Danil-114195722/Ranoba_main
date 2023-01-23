from django.urls import path
from . import views


urlpatterns = [
    path('read/<str:name_book>/<int:chapter>', views.read, name='read_book'),
    path('listen/<str:name_audio>/<int:chapter>', views.listen, name='listen_audio'),
    path('book_review/<str:book_title>', views.book_review, name='book_review'),
]
