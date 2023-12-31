[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?style=flat&logo=FastAPI&logoColor=ffffff&color=043A6B)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy&logoColor=ffffff&color=043A6B)](https://pypi.org/project/SQLAlchemy/)
[![Alembic](https://img.shields.io/badge/-Alembic-464646?style=flat&logo=Alembic&logoColor=ffffff&color=043A6B)](https://pypi.org/project/alembic/)
[![Pydantic](https://img.shields.io/badge/-Pydantic-464646?style=flat&logo=Pydantic&logoColor=ffffff&color=043A6B)](https://pypi.org/project/pydantic/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=Pydantic&logoColor=ffffff&color=043A6B)](https://www.postgresql.org/)
# Test_task-2_Bewise
Тестовое задание №2 Bewise.ai

Задание:
 - С помощью Docker (предпочтительно - docker-compose) развернуть образ с любой опенсорсной СУБД (предпочтительно - PostgreSQL). Предоставить все необходимые скрипты и конфигурационные (docker/compose) файлы для развертывания СУБД, а также инструкции для подключения к ней. Необходимо обеспечить сохранность данных при рестарте контейнера (то есть - использовать volume-ы для хранения файлов СУБД на хост-машине.
 - Реализовать веб-сервис со следующими REST методами:
    - Создание пользователя, POST:
      - Принимает на вход запросы с именем пользователя;
      - Создаёт в базе данных пользователя заданным именем, так же генерирует уникальный идентификатор пользователя и UUID токен доступа (в виде строки) для данного пользователя;
      - Возвращает сгенерированные идентификатор пользователя и токен.
    - Добавление аудиозаписи, POST:
      - Принимает на вход запросы, содержащие уникальный идентификатор пользователя, токен доступа и аудиозапись в формате wav;
      - Преобразует аудиозапись в формат mp3, генерирует для неё уникальный UUID идентификатор и сохраняет их в базе данных;
      - Возвращает URL для скачивания записи вида http://host:port/record?id=id_записи&user=id_пользователя.
    - Доступ к аудиозаписи, GET:
      - Предоставляет возможность скачать аудиозапись по ссылке из п 2.2.3.
 - Для всех сервисов метода должна быть предусмотрена предусмотрена обработка различных ошибок, возникающих при выполнении запроса, с возвращением соответствующего HTTP статуса.
 - Модель данных (таблицы, поля) для каждого из заданий можно выбрать по своему усмотрению.
 - В репозитории с заданием должны быть предоставлены инструкции по сборке докер-образа с сервисами из пп. 2. и 3., их настройке и запуску. А также пример запросов к методам сервиса.
 - Желательно, если при выполнении задания вы будете использовать docker-compose, SQLAlchemy,  пользоваться аннотацией типов.  

### Запуск проекта
- Скачать и установить [Docker](https://docs.docker.com/get-docker/)
- Клонировать репозиторий ```git clone git@github.com:Hastred45/bewise_task_2.git``` 
- В корне директории bewise_task_2 создать файл .env и заполнить его по примеру .env.example
- В папке infra выполнить команду ```docker compose up -d```
- Перейти по адресу ```http://127.0.0.1:8000/docs```  

### Примеры запросов

1. Создание нового пользователя  
_**POST .../auth/**_
```JSON
{
  "id": 2,
  "UUID": "9ef9af5c-9f4a-45ce-858a-8a1598db51c5"
}
```
![1](https://raw.github.com/Hastred45/bewise_task_2/7b36f07b06e364099fae98d5e0ece749a6d91c59/Screenshot_13.png)


2. Загрузка аудиофайла для конвертации
_**POST .../**_
```JSON
{
  "url": "http://127.0.0.1:8000/record?id=2&user=2"
}
```
![1](https://raw.github.com/Hastred45/bewise_task_2/7b36f07b06e364099fae98d5e0ece749a6d91c59/Screenshot_14.png)

3. Скачивание аудиофайла
_**POST .../record/**_
```
 content-disposition: attachment; filename="barradeen-first-girl-talking-to-me.mp3" 
 content-length: 1691315 
 content-type: audio/mpeg 
 date: Sun,11 Jun 2023 11:17:29 GMT 
 server: uvicorn 
```
![1](https://raw.github.com/Hastred45/bewise_task_2/7b36f07b06e364099fae98d5e0ece749a6d91c59/Screenshot_15.png)


