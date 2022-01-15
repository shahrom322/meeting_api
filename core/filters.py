import django_filters

from core.models import CustomUser


class UserFilter(django_filters.FilterSet):
    """Фильтр по полям модели CustomUser."""

    class Meta:
        model = CustomUser
        fields = ['sex', 'first_name', 'last_name']
