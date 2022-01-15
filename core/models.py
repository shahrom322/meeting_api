from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from core.managers import CustomUserManager
from core.services import send_message


class CustomUser(AbstractBaseUser):
    """Модель пользователя."""

    GENDER = (
        ('M', 'Мужской'),
        ('F', 'Женский')
    )

    avatar = models.ImageField('Аватар', upload_to='avatars')
    sex = models.CharField('Пол', max_length=1, choices=GENDER)
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    email = models.EmailField('Почта', unique=True)
    likes_from_users = models.ManyToManyField(
        'self', blank=True, symmetrical=False,
        verbose_name='Лайки от пользователей', related_name='likes_for'
    )
    likes_for_users = models.ManyToManyField(
        'self', blank=True, symmetrical=False,
        verbose_name='Лайки пользователям', related_name='likes_from'
    )
    longitude = models.DecimalField(
        'Долгота', max_digits=9, decimal_places=6, blank=True, null=True
    )
    latitude = models.DecimalField(
        'Широта', max_digits=9, decimal_places=6, blank=True, null=True
    )

    def like_user(self, user):
        """Добавляет в QuerySet likes_for_users переданный объект
         пользователя. Так же добавляет в QuerySet likes_from_users
         переданного пользователя объект self.
         В том случае, если симпатия взаимна, вызывает функцию send_message."""

        self.likes_for_users.add(user)
        user.likes_from_users.add(self)
        if self.is_mutual_sympathy(user):
            send_message(self, user.email)
            send_message(user, self.email)

    def is_mutual_sympathy(self, user):
        """Проверяет взаимную симпатию по наличию переданного пользователя
        в QuerySet likes_from_users."""

        return user in self.likes_from_users.all()

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'
