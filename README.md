# Тестовое задание на позицию Python разработчика / Effective Mobile

Тестовое задание представляет собой платформу для управления заказами в кафе.

Как запустить проект:
1. Клонировать репозиторий к себе ```git clone git@github.com:OlegPrizov/effective_mobile_test.git```
2. Перейти в репозиторий ```cd effective_mobile_test/```
3. Создать и активировать виртуальное окружение ```python3 -m venv venv```
4. Установить зависимости ```pip install -r requirements.txt```
5. Запустить проект ```python manage.py runserver```
6. Перейти в браузере по ссылке http://127.0.0.1:8000/

Также реализовано API:
1. POST /api/auth/users/ – зарегистрировать нового пользователя
2. GET /api/auth/users/me/ – получить текущего пользователя
3. POST /api/auth/jwt/create/ – получить jwt токен
4. POST /api/auth/jwt/refresh/ – обновить jwt токен
5. POST api/orders/ – добавляет заказ
6. DELETE /orders/{id}/ – удаляет заказ 
7. PUT /orders/{id}/ - изменяет заказ
8. GET /orders/ – отображает все заказы

Дополнительно документация API доступна по api/docs/

Проект реализован на Python 3.9.19

*Автор: [Призов Олег](https://github.com/OlegPrizov/)* 