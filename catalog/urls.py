from django.urls import path
from . import views


urlpatterns = [
    path('', views.choice_category, name='catalog'),
]
