# Create your models here.
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name} / {self.location}"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=300)
    publication_date = models.DateField()
    pages = models.IntegerField()
    author = models.ManyToManyField(Author, related_name="books")
    publisher = models.ForeignKey(
        Publisher, on_delete=models.SET_NULL, null=True, related_name="books"
    )
    summary = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField(
        Category, through="BookCategory", related_name="books"
    )
    price = models.IntegerField()

    def __str__(self):
        return self.title


class BookCategory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("book", "category")
