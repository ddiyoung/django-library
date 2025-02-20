from rest_framework import serializers
from ..models import Like, Review


class LikeSerializer(serializers.ModelSerializer):

    review = serializers.PrimaryKeyRelatedField(
        queryset=Review.objects.all(), write_only=True
    )

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Like
        fields = ["review", "user", "status"]
