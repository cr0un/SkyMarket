# SkyMarket

___

## Бэкенд функционал:

- Авторизация и аутентификация пользователей.
- Распределение ролей между пользователями (пользователь и админ).
- Восстановление пароля через электронную почту.
- CRUD для объявлений на сайте.
- Разграничение доступа к редактированию/удалению объявлений.
- Под каждым объявлением пользователи могут оставлять отзывы.
- В заголовке сайта можно осуществлять поиск объявлений по названию.

___

## Стэк:

![Python3.10](https://img.shields.io/badge/-Python3.10-blue)
![Django](https://img.shields.io/badge/-Django-blue)
![DjangoREST](https://img.shields.io/badge/-DjangoREST-blue)
![Postgres](https://img.shields.io/badge/-Postgres-blue)
![Docker](https://img.shields.io/badge/-Docker-blue)

___

## Запуск:

1) Без фронт-части:
    
    В консоли введите python `./SkyMarket/manage.py startserver`

2) С фронт-частью(она сама по себе по какой-то причине работает криво, писал не я):

    - Перейдите в папку market_postgres командой `cd market_postgres`
    - Запустите контейнер командой `docker-compose up --build -d`
    - Возвращаемся в исходную папку командой `cd ..`
    - Запускаем сервер командой `./SkyMarket/manage.py startserver`
    - Фронт-часть будет доступна по адресу localhost:3000
