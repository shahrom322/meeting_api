## API для онлайн знакомств. 

[Демо-версия](https://meeting-now-api.herokuapp.com/) сайта расположена на бесплатном хостинге heroku.com

![site](https://sun9-50.userapi.com/impf/u679pMkN5IbME0dU_VKWDTxIHd0jDfE0VCxKFw/I4Bl1686IUk.jpg?size=1382x961&quality=96&sign=5036ca2348af1960c60d896b598d3c21&type=album "site")
<hr>

 Тестовое задание по Django-rest-framework.
* Реализована кастомная модель пользователя.
* При регистрации нового пользователя обрабатывается его аватарка: в модуле services.py функция watermark_photo добавляет на фотографию водяной знак.
* При переходе авторизованного пользователя на эндпоинт /api/clients/{id}/match/ пользователю, чей идентификатор указан в пути, устанавливается симпатия. В том случае если эта симпатия взаимна, то обоим пользователям отправляется на почту письмо.
* Реализована фильтрация django-filters по пользователям. В модуле filters создан кастомный фильтр для определения дистанции от пользователя, который отправил запрос. Пользователь может ввести значение максимального расстояния, в БД отправляется ORM запрос, где вычисляется расстояние до каждого пользователя.
<hr>

## Установка
Клонируем репозиторий:
    
    git clone https://github.com/shahrom322/meeting_api.git

Создаем виртуальную среду:

    python -m venv venv

Активируем её:

    source venv/bin/activate

Устанавливаем зависимости:

    pip install -r requirements.txt

Создайте файл .env со следущими переменными и введите нужные значения для почтового аккаунта (используется smtp.gmail.com):

`DEBUG=True`
`SECRET_KEY=your_django_secret_key`
`EMAIL_HOST_USER=your_email@gmail.com`
`EMAIL_HOST_PASSWORD=your_email_password`


В качестве БД в отладочном режиме можно использовать sqlite3.
Для этого в settings.py установите дефолтное значение `DATABASES`

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'sqlite3'),
        }
    }
Значение `ALLOWED_HOST` установите в `['*']`

Затем примините миграции:

    python manage.py migrate


И запустите сервер:


    python manage.py runserver

