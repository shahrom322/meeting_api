from django.contrib.auth.base_user import BaseUserManager
from django.core.files.uploadedfile import InMemoryUploadedFile

from core.services import watermark_photo


class CustomUserManager(BaseUserManager):
    """Диспетчер кастомной модели пользователя, определяет электронную
     почту уникальным идентификатором для аутентификации."""

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Поле с почтой обязательно для заполнения')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        watermarked_image = watermark_photo(user.avatar)
        user.avatar = InMemoryUploadedFile(
            watermarked_image, None, user.avatar.name,
            'image/jpeg', watermarked_image.tell, None
        )
        user.set_password(password)
        user.save()
        return user
