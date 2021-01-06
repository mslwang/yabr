from rest_framework import viewsets

from .models import Author, AuthorToBook, Book
from .serializers import (AuthorSerializer, AuthorToBookSerializer,
                          BookSerializer)


class AuthorViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update`, and `destroy` actions for authors.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorToBookViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update`, and `destroy` actions for ratings.
    """
    queryset = AuthorToBook.objects.all()
    serializer_class = AuthorToBookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update`, and `destroy` actions for ratings.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
