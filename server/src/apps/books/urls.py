from django.urls import path

from .views import AuthorToBookViewSet, AuthorViewSet, BookViewSet

# How would I do this more efficiently?

author_list_all = AuthorViewSet.as_view({'get': 'list'})

author_list_book = AuthorToBookViewSet.as_view({'get': 'retrieve'})

book_list_all = BookViewSet.as_view({'get': 'list'})

book_list_specific = BookViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    path('author/', author_list_all, name='author-list'),
    path('author/<int:pk>/', author_list_book, name='author-detail'),
    path('book/', book_list_all, name='book-list'),
    path('book/<int:pk>/', book_list_specific, name='book-detail')
]
