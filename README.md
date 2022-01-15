## Сайт для онлайн знакомств

API для сайта знакомств. 

Демо-версия сайта расположена на бесплатном хостинге [heroku.com](https://meeting-now-api.herokuapp.com/)


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

