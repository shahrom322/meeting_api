import io

from PIL import Image


def watermark_photo(input_image_path):
    """Обрабатывает фотографию. Добавляет водяной знак watermark_sample.png.
    :param input_image_path: Путь фотографии на которую хотим добавить знак.
    :return io.BytesIO: Новая фотография возвращается из буфера в байтовом
     формате."""

    with Image.open(input_image_path) as base_image,\
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
