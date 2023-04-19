### API для Yatube

Проект API для Yatube.
Вся логика описана в отдельном приложении "api".

```
Описаны сериализаторы для моделей и view-функции. 
Post, Group, Comment, Follow.
```

```
Модели Post и Comment выполняют полный набор CRUD функций.
URL подключены с помощью DefaultRouter.

Модель Group позволяет делать только GET-запросы.
Модель Follow позволяет делать только GET и POST-запросы.
Так же есть адреса для получения и обновления токена.
```

```
Отправим POST-запрос на 'http://127.0.0.1:8000/api/v1/posts/'
{
  "text": "Текст.",
  "group": 1
}
Response:
{
	"id": 1,
	"text": "Текст.",
	"author": "anikel",
	"image": null,
	"group": 1,
	"pub_date": "2023-04-19T18:48:47.476426Z"
}
```

```
Отправим GET-запрос на 'http://127.0.0.1:8000/api/v1/posts/1/comments/'

Response:
[
	{
		"id": 1,
		"author": "anikel",
		"post": 1,
		"text": "Текст.",
		"created": "2023-04-19T18:51:19.670396Z"
	}
]
```

###  Как работать с проектом.
Клонировать репрозиторий.
Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Технологии

- Python 3.9.10
- Django 3.2.16
- django-filter==23.1
- djangorestframework==3.12.4
- djangorestframework-simplejwt==5.2.2
- djoser==2.2.0
- requests==2.26.0
