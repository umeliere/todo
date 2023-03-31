<h1>Инструкция по установки todo...</h1>

<h2>Установить к себе репозиторий:</h2>
```
git clone https://github.com/umeliere/todo.git
```
---

<h4>Создать файл .env в папке todo/todo(где находится файл settings.py)<br>
В него занести следующие данные:<br></h4>

```
DEBUG=True
SECRET_KEY=django-insecure-t1l3bst+gvcus#k8)(uc52ho$uf83l)_3z87npaw%3be*1xk3t
EMAIL_HOST=smtp.yandex.ru
EMAIL_PORT=465
EMAIL_HOST_USER=umeliere.answer@yandex.ru
DEFAULT_FROM_EMAIL=umeliere.answer@yandex.ru
EMAIL_HOST_PASSWORD=TodoList
EMAIL_USE_SSL=True
```

--- 

<h2>Последнии шаги</h2>

Установить django командой(версия Python >= 3.8, django=4):

```
pip install -r requirements.txt
```

Произвести миграции:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

Создать суперпользователя:
```
python3 manage.py createsuperuser
```

Запустить сервер(по умолчанию http://localhost:8000):
```
python3 manage.py runserver
```


