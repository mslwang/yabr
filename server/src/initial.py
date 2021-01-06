# source: https://stackoverflow.com/questions/41507845/how-to-write-a-pandas-dataframe-to-existing-django-model

import datetime as dt
import os
import sys
from pathlib import Path

import django
import pandas as pd

sys.path.append('.')  # add path to project root dir
os.environ["DJANGO_SETTINGS_MODULE"] = "backend.settings"

# for more sophisticated setups, if you need to change connection settings (e.g. when using django-environ):
#os.environ["DATABASE_URL"] = "postgres://myuser:mypassword@localhost:54324/mydb"

# Connect to Django ORM
django.setup()

# process data
ratings = pd.read_csv(Path('..', 'data', 'ratings.csv').resolve())
books = pd.read_csv(Path('..', 'data', 'books.csv').resolve())

books['original_publication_year'].fillna(0, inplace=True)

from apps.books.models import Book
from apps.ratings.models import Rating
from apps.users.models import User

# def createUser(id):
#     return User(id=id, name=" ", username=" ", password=" ")

# book_instances = {book.book_id:Book(id=book.book_id, isbn=book.isbn, original_publication_year=book.original_publication_year, title=book.original_title, image_url=book.image_url) for book in books.itertuples()}

# Book.objects.bulk_create(book_instances.values())

# user_instances = {id:createUser(id) for id in range(1, ratings.user_id.max()+1)}

# User.objects.bulk_create(user_instances.values())

# DateTimeField Rating.time_created received a naive datetime (2021-01-06 22:39:24.038879) while time zone support is active.
# Can use timezone corrected times
# Used rating[0] when it worked, rating.Index should work well but haven't tried
model_instances = [
    Rating(rating=rating.rating,
           user_id=User.objects.get(id=rating.user_id),
           book_id=Book.objects.get(id=rating.book_id),
           time_created=dt.datetime.now())
    for rating in ratings.itertuples()
    if rating.Index <= 100
]

Rating.objects.bulk_create(model_instances)
