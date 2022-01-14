from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """Диспетчер кастомной модели пользователя, определяет электронную
     почту уникальным идентификатором для аутентификации."""

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Поле с почтой обязательно для заполнения')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
