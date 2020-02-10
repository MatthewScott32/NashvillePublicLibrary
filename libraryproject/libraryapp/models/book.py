from django.db import models
from .library import Library
from .librarian import Librarian
from django.urls import reverse

class Book(models.Model):

    Title = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=50)
    Author = models.CharField(max_length=50)
    YearPublished = models.IntegerField()
    Location = models.ForeignKey(Library, on_delete=models.CASCADE)
    Librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)

    # class Meta:
    #     verbose_name = ("Book")
    #     verbose_name_plural = ("Books")

    # def __str__(self):
    #     return self.Title

    # def get_absolute_url(self):
    #     return reverse("Book_detail", kwargs={"pk": self.pk})