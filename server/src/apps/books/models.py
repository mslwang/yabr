from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)


class Book(models.Model):
    isbn = models.CharField(max_length=10)
    original_publication_year = models.FloatField()
    title = models.CharField(max_length=60)
    description = models.TextField()
    image_url = models.CharField(max_length=255)


class AuthorToBook(models.Model):
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
