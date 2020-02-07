from django.db import models
from .library import Library
from .librarian import Librarian

class Book(models.Model):

    Title = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=50)
    Author = models.CharField(max_length=50)
    YearPublished = models.IntegerField()
    Location = models.ForeignKey(Library, on_delete=models.CASCADE)
    Librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)