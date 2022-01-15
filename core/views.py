from rest_framework import generics, permissions

from core.filters import UserFilter
from core.models import CustomUser
from core.serializers import (
    CreateCustomUserSerializer,
    UserMatchSerializer,
    UserListSerializer
)


class CreateUserAPIView(generics.CreateAPIView):
    """API контроллер для регистрации нового пользователя."""

    queryset = CustomUser.objects.all()
    serializer_class = CreateCustomUserSerializer
    permission_classes = [permissions.AllowAny]


class UserMatchAPIView(generics.RetrieveAPIView):
    """API контроллер для отправки пользователю лайка.
    path 'clients/<int:pk>/match/' где pk это идентификатор пользователя,
    которому предназначен лайк """

    serializer_class = UserMatchSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        like_for_user = generics.get_object_or_404(
            CustomUser, id=self.kwargs['pk']
        )
        user.like_user(like_for_user)
        return like_for_user


class UserListAPIView(generics.ListAPIView):
    """API контроллер для вывода списка пользователей с возможностью фильтрации по
    полу, имени, фамилии и максимального расстояния в километрах."""

    queryset = CustomUser.objects.all()
    serializer_class = UserListSerializer
    filter_class = UserFilter
    permission_classes = [permissions.IsAuthenticated]
