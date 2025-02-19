from unicodedata import category

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
    author = AuthorSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    publisher = PublisherSerializer(read_only=True)

    author_ids = serializers.PrimaryKeyRelatedField(  # ✅ POST/PATCH 시 사용
        many=True, queryset=Author.objects.all(), write_only=True
    )
    categories_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Category.objects.all(), write_only=True
    )
    publisher_ids = serializers.PrimaryKeyRelatedField(
        queryset=Publisher.objects.all(), write_only=True
    )

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "publication_date",
            "pages",
            "summary",
            "author",
            "categories",
            "publisher",
            "author_ids",
            "categories_ids",
            "publisher_ids",
        ]

    def create(self, validated_data):
        author_ids = validated_data.pop("author_ids", [])
        categories_ids = validated_data.pop("categories_ids", [])
        publisher_ids = validated_data.pop("publisher_ids", None)

        instance = super().create(validated_data=validated_data)

        instance.author.set(author_ids)
        instance.categories.set(categories_ids)

        if publisher_ids:
            instance.publisher = publisher_ids
            instance.save()

        return instance

    def update(self, instance, validated_data):
        author_ids = validated_data.pop("author_ids", [])
        categories_ids = validated_data.pop("categories_ids", [])
        publisher_ids = validated_data.pop("publisher_ids", None)

        instance = super().update(instance, validated_data)

        # Update author
        if author_ids:
            instance.author.set(author_ids)

        if categories_ids:
            instance.categories.set(categories_ids)

        if publisher_ids:
            instance.publisher = publisher_ids
            instance.save()

        return instance
