from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)


class AuthorToBooks(models.Model):
    author_id = models.ForeignKey()
    book_id = models.ForeignKey()


class Book(models.Model):
    isbn = models.IntegerField(unique=True)
    isbn13 = models.IntegerField(unique=True)
    original_publication_year = models.IntegerField()
    title = models.CharField()
    description = models.CharField()
    image_url = models.CharField()
