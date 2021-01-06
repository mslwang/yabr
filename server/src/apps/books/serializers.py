from rest_framework import serializers

from .models import Author, AuthorToBook, Book


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class AuthorToBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthorToBook
        fields = '__all__'
        depth = 1
