### API для Yatube

Вся логика описана в приложении API

```
Описаны сериализаторы для моделей и вьюфункции. 
Post, Group, Comment, Follow.
```

```
Описаны следующие урл адреса:
'api/v1/posts'
'api/v1/groups'
'api/v1/posts/(?P<post_id>\d+)/comments'
'api/v1/follow'
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
