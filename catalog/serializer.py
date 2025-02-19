from rest_framework import serializers

from .models import Book, Author, Category, Publisher


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name", "bio"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ["id", "name", "location"]


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    publisher = PublisherSerializer(read_only=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "publication_date",
            "pages",
            "summary",
            "authors",
            "categories",
            "publisher",
        ]
