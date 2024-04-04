from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserCreateSerializer(serializers.Serializer):
    usermane = serializers.CharField()
    password = serializers.CharField()

    def validated_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError("User already exists!")

class UserLoginSerializer(serializers.Serializer):
    usermane = serializers.CharField()
    password = serializers.CharField()