from rest_framework import generics, permissions

from core.models import CustomUser
from core.serializers import CreateCustomUserSerializer


class CreateUserAPIView(generics.CreateAPIView):
    """API контроллер для регистрации нового пользователя."""

    queryset = CustomUser.objects.all()
    serializer_class = CreateCustomUserSerializer
    permission_classes = [permissions.AllowAny]
