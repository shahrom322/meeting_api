import io

from PIL import Image
from django.core.mail import send_mail
from geopy.distance import geodesic


def watermark_photo(input_image_path):
    """Обрабатывает фотографию. Добавляет водяной знак watermark_sample.png.
    :param input_image_path: Путь фотографии на которую хотим добавить знак.
    :return io.BytesIO: Новая фотография возвращается из буфера в байтовом
     формате."""

    with Image.open(input_image_path) as base_image, \
            Image.open('watermark/watermark_sample.png') as watermark:
        width, height = base_image.size
        # Создаем новое изображение с такими же размерами,
        # добавляем альфа канал.
        rgba_image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        rgba_image.paste(base_image, (0, 0))
        # Вставляем водяной знак в верхний левый угол изображения,
        # и маскируем его самим собой.
        rgba_image.paste(watermark, (0, 0), mask=watermark)
        # Убираем альфа канал, что бы сохранить в JPG.
        rgb_image = rgba_image.convert('RGB')
        # Используем байтовый буфер.
        img_io = io.BytesIO()
        rgb_image.save(img_io, format='JPEG')
        return io.BytesIO(img_io.getvalue())


def send_message(user, address):
    """Отправляет письмо о взаимной симпатии.
    :param user: CustomUser который будет указан в письме.
    :param address: почтовый адрес, на который будет отправлено письмо."""

    return send_mail(
        'У Вас взаимная симпатия.',
        f'Вы понравились {user.first_name}! Почта участника: {user.email}',
        None,
        [address],
        fail_silently=False
    )


def get_distance(first_user_coords: tuple,
                 second_user_coords: tuple
                 ) -> float:
    """Рассчитывает расстояние между двумя пользователями.
    :param first_user_coords: Кортеж координат (широта, долгота) начальной точки.
    :param second_user_coords: Кортеж координат (широта, долгота) точки до которой
    рассчитываем координаты.
    :return float: Расстояние в километрах."""

    return geodesic(first_user_coords, second_user_coords).kilometers
