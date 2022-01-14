from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from core.managers import CustomUserManager


class CustomUser(AbstractBaseUser):
    """Модель пользователя."""

    GENDER = (
        ('M', 'Мужской'),
        ('F', 'Женский')
    )

    avatar = models.ImageField('Аватар', upload_to='avatars')
    male = models.CharField('Пол', max_length=1, choices=GENDER)
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    email = models.EmailField('Почта', unique=True)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'
