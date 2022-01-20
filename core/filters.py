import django_filters
from django.db.models import F
from django.db.models.functions import Sin, Cos, ACos, Radians

from core.models import CustomUser


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
        # Рассчитываем расстояние на поверхности земли по формуле:
        #       cos(d) = sin(φА)·sin(φB) + cos(φА)·cos(φB)·cos(λА − λB),
        # где φА и φB — широты, λА, λB — долготы данных точек,
        # d — расстояние между пунктами, измеряемое в радианах длиной дуги большого круга земного шара.

        # Расстояние между пунктами, измеряемое в километрах, определяется по формуле:
        #       L = d·R,
        # где R = 6399 км — средний радиус земного шара
        # http://osiktakan.ru/geo_koor.htm

        queryset = possible_users.annotate(
            distance=6399 * (ACos(
                Sin(Radians(F('latitude'))) * Sin(Radians(current_user.latitude)) +
                Cos(Radians(F('latitude'))) * Cos(Radians(current_user.latitude)) *
                Cos(Radians(F('longitude')) - Radians(current_user.longitude)))
            )
        ).filter(distance__lte=value)
        return queryset

    class Meta:
        model = CustomUser
        fields = ['sex', 'first_name', 'last_name', 'max_distance']
