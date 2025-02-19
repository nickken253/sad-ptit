from django.urls import path
from .views import book_list, book_detail, add_book

urlpatterns = [
    path('', book_list, name='book_list'),
    path('<str:book_id>/', book_detail, name='book_detail'),
    path('add/', add_book, name='add_book'),
]
