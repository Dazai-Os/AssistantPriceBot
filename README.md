# Assistant Price Bot

Assistant Price - это телеграм-бот для отслеживания цен с сайта [Ситилинк](https://www.citilink.ru).
Пользователь отправляет ссылку товара с ситилинка и заносится в базу данных, для последующего отслеживания выбранного им товара. Если пользователь вводит неккоректную ссылку, ему об этом сообщится. Или если он пытается отслеживать еще один такой же товар.

Также пользователь может посмотреть все отслеживаемые им товары, удалить или перейти по ссылке товара.

Команда \help для помощи пользователю

__Добавление отслеживаемых товаров__

![](https://github.com/Dazai-Os/AssistantPricebot/blob/master/other/photo_2022-02-20_21-02-22.jpg)

__Просмотр товаров__

![](https://github.com/Dazai-Os/AssistantPricebot/blob/master/other/photo_2022-02-20_21-02-17.jpg)

Попробовать: [AssistantPricebot](https://t.me/AssistantPricebot)

____
>__Стек технологий__:
* asyncio
* aiogram - телеграм бот
* request + bs4 - парсер
* asyncpg - Работа с базой данных Postgresql

____
## ___Сборка репозитория и локальный запуск___

Выполните в консоли:

`git clone https://github.com/Dazai-Os/AssistantPricebot`

`pip install -r requirements.txt`

### Настройка
создайте файл .env и добавьте туда следующие настройки

`BOT_NAME=Имя бота`

`BOT_TOKEN=токен бота`

`ADMINS=id админа`

`DB_USER=имя пользователя базы данных`

`PG_PASSWORD=postgres пароль`

`DB_PASS=пароль от базы данных`

`DB_NAME=имя базы данных`

`DB_HOST=Хост базы данных`


### Запуск бота 
в консоле находясь в корневой папке бота запустите скрипт bot.py

`python bot.py`
