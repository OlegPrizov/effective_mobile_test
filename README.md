# Тестовое задание на позицию Python разработчика / Effective Mobile

Тестовое задание представляет собой платформу для управления заказами в кафе.

Как запустить проект:
1. Клонировать репозиторий к себе ```git clone git@github.com:OlegPrizov/effective_mobile_test.git```
2. Перейти в репозиторий ```cd effective_mobile_test/```
3. Создать и активировать виртуальное окружение ```python3 -m venv venv```
4. Установить зависимости ```pip install -r requirements.txt```
5. Запустить проект ```python manage.py runserver```

Также реализовано API:
POST /api/auth/users/ – зарегистрировать нового пользователя
GET /api/auth/users/me/ – получить текущего пользователя
POST /api/auth/jwt/create/ – получить jwt токен
POST /api/auth/jwt/refresh/ – обновить jwt токен
POST api/orders/ – добавляет заказ
DELETE /orders/{id}/ – удаляет заказ 
PUT /orders/{id}/ - изменяет заказ
GET /orders/ – отображает все заказы

*Автор: [Призов Олег](https://github.com/OlegPrizov/)* 