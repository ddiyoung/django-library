from rest_framework import serializers
from yaml import serialize_all

from ..models import Review

from catalog.models import Book
from users.models import User


class ReviewSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(), write_only=True
    )

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    user_name = serializers.CharField(source="user.username", read_only=True)
    book_title = serializers.CharField(source="book.title", read_only=True)
    like_cnt = serializers.SerializerMethodField(read_only=True)
    hate_cnt = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Review
        fields = [
            "book",
            "book_title",
            "user",
            "user_name",
            "title",
            "content",
            "like_cnt",
            "hate_cnt",
        ]

    def get_like_cnt(self, obj):
        return obj.likes.filter(status="like").count()

    def get_hate_cnt(self, obj):
        return obj.likes.filter(status="hate").count()
