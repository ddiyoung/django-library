from rest_framework import serializers

from catalog.models import Book
from users.models import User
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(), write_only=True
    )

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    book_title = serializers.CharField(source="book.title", read_only=True)
    user_name = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "updated_at",
            "book",
            "book_title",
            "user",
            "user_name",
        ]

    def create(self, validated_data):
        validated_data.pop("status", None)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop("user", None)
        return super().update(instance, validated_data)
