# Веб-приложение для управления базой данных списка пользователей.

Список полей: фото, фамилия, имя, отчество, день рождения, номер телефона, статус (не активирован/активирован/удалён).

Функционал приложения

    список пользователей с полями: фамилия, имя, отчество, день рождения, номер телефона, статус
    поиск по этим же полям
    просмотр профиля пользователя с данными
    добавление/изменение/удаление пользователя

#### Фреймворк: Django, сервер баз данных: PostgreSQL, поле фото имеет возможность загрузить фотографию

### Настройка проекта

Создайте `.env` файл в корне репозитория:

```bash
cp .env.conf .env
```

Внесите при необходимости корректировки в переменные окружения.


### Сборка образов и запуск контейнеров

В корне репозитория выполните команду:

```bash
docker-compose up --build
```

### Остановка контейнеров

Для остановки контейнеров выполните команду:

```bash
docker-compose stop
```

### Инициализация проекта

Миграции происходят автоматически.

Команды выполняются внутри контейнера приложения:

```bash
docker-compose exec app bash
```

#### Создание суперпользователя

```bash
python manage.py createsuperuser
```

Проект доступен по адресу http://127.0.0.1:8000


Данные для входа на vps:
OS: Ubuntu 20.04
IP: 93.189.46.123
Логин: root
Пароль: iyUy72D28vks