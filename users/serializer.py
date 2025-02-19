from rest_framework import serializers
from .models import User
from django.contrib.auth.models import Group


class SignInSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
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
        )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.groups.add(Group.objects.get(name="Customer"))
        return user
