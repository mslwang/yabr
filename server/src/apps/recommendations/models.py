from django.db import models


# Create your models here.
class Recommendation(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    book_id = models.ForeignKey('Book', on_delete=models.CASCADE)
    batch_id = models.ForeignKey('Batch', on_delete=models.CASCADE)
    time_created = models.DateTimeField()


class Batch(models.Model):
    time_created = models.DateTimeField()
