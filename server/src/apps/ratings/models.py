from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from ..books.models import Book
from ..users.models import User


# Create your models here.
class Rating(models.Model):
    rating = models.IntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(5)])
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    time_created = models.DateTimeField()
