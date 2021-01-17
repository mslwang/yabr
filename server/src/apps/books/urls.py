from django.urls import path

from .views import AuthorToBookViewSet, AuthorViewSet, BookViewSet

# How would I do this more efficiently?

authors_list_all = AuthorViewSet.as_view({'get': 'list'})

authors_list_book = AuthorToBookViewSet.as_view({'get': 'retrieve'})

books_list_all = BookViewSet.as_view({'get': 'list'})

books_list_specific = BookViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    path('authors/', authors_list_all, name='authors-list'),
    path('authors/<int:pk>/', authors_list_book, name='authors-detail'),
    path('books/', books_list_all, name='books-list'),
    path('books/<int:pk>/', books_list_specific, name='books-detail')
]
