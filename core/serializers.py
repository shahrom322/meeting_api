from rest_framework import serializers

from core.models import CustomUser


class CreateCustomUserSerializer(serializers.ModelSerializer):
    """Класс сериалайзера для создания нового пользователя."""

    class Meta:
        model = CustomUser
        fields = [
            'avatar', 'male', 'first_name',
            'last_name', 'email', 'password',
        ]

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class UserMatchSerializer(serializers.ModelSerializer):
    """Класс сериалайзера для отображения почты пользователя."""

    class Meta:
        model = CustomUser
        fields = ['email']
