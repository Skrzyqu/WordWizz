from django.urls import path
from .views import word_list

urlpatterns = [
    path('words/', word_list, name='word_list'),
]