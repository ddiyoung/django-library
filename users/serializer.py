from rest_framework import serializers
from .models import User


class SignInSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    full_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "full_name",
            "phone_number",
            "address",
            "date_of_birth",
            "user_type",
        )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
