import django_filters

from core.models import CustomUser
from core.services import get_distance


class UserFilter(django_filters.FilterSet):
    """Фильтр по полям модели CustomUser."""

    max_distance = django_filters.CharFilter(
        method='filter_max_distance', label='Максимальное расстояние(км)'
    )

    def filter_max_distance(self, queryset, name, value):
        """Пользовательский фильтр. Фильтрует пользователей по их максимальному расстоянию value
        от пользователя, который отправил запрос."""

        current_user = self.request.user
        possible_users = queryset.exclude(id=current_user.id)
        result_id_list = []
        for possible_user in possible_users:
            distance = get_distance(
                (current_user.latitude, current_user.longitude),
                (possible_user.latitude, possible_user.longitude)
            )
            if distance < float(value):
                result_id_list.append(possible_user.id)
        return queryset.filter(id__in=result_id_list)

    class Meta:
        model = CustomUser
        fields = ['sex', 'first_name', 'last_name', 'max_distance']
