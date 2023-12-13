# __Эндпоинт ценообразования для marketplace__
___
## Исползуемые технологии

|`python` | `django` | `django rest framework` | `drf-yasg` | `postgresql` |
| ------ | ------ |------ |------ |------ |

|`cors` | `OOP` | `simple jwt` |
| ------ |-------| ------ |
___

# О проекте 
> Удобное REST API приложение для выставление цены продавцом с условием дополнительных надбавок продающей площадки.

## ___Функции___
- _Для искользования финкцианала пользователю необходимо пройти регистарцию_
- _Для пользования эндпоинтом пользователю необходимо зарегестрироваться как продавец_
- _Пользоатель вводит ту сумму, котороую он хотел бы получить со своего продукта, и получает сумму которая будет выводиться на продающей площадке_
___

## Сущности системы
  ### Привычка
  * цена продавца
  * цена маркетплейса(__автоматически__)


### Пользователь
* почта
* пароль
* авторизоваться как (__опционально__)

## Документация API
Документация для API реализована с помощью drf-yasg и находится на следующих эндпоинтах:
* http://127.0.0.1:8000/docs/
* http://127.0.0.1:8000/redoc/

## CORS
Для безопасности API реализован CORS с помощью django-cors-headers. 

В модуле ``settings.py`` необходимо внести изменения в следующие настройки, если у вас есть сторонние домены, обращающиеся к вашему API:

```
CORS_ALLOWED_ORIGINS = [
    "https://read-only.example.com",
    "https://read-and-write.example.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://read-and-write.example.com",
]
```

## Запуск проекта с помощью IDE:

* Склонировать репозиторий в IDE
  
  В терминале ввести команду:
  ```
  git clone https://github.com/YahontovE/Habits.git
* Установить вирутальное окружение

  В терминале ввести команду:
  ```
  python3 -m venv venv
  ```
* Активировать виртуальное окружение

  В терминале ввести команду:
  ```
  source venv/bin/activate
  ```
* Установить зависимости

  В терминале ввести команду:
  ```
  pip install -r requirements.txt
  ```
* Создать файл ``.env``. Его необходимо заполнить данными из файла ``.env.sample``
* Создайте Базу данных (в данной работе используется PostgreSQL)
* Создать и применить миграции

  В терминале ввести следующие команды:
  ```
  python3 manage.py makemigrations
  ```
  ```
  python3 manage.py migrate
  ```
* Создать суперпользователя ``csu.py``
* Создать пользователя с флагом продавец ``cus.py``
* Создать пользователя без флага продавец ``cu.py``

  В терминале ввести команду:
  ```
  python3 manage.py csu

* Запустить сервер

  В терминале ввести команду:
  ```
  python3 manage.py runserver
  ```
  
- После регистрации идет получение токена: через указания данных(Поля `email` и `password`) производится `post`-запрос.
При получении ответа, нужно скопировать значение ключа `access` и при дальнейшем пользовании в поле авторизации прописывать
`Bearer {token}`