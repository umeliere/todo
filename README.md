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

По умолчанию, почта на которую приходят письма: umeliere.answer@yandex.ru.<br> Вы можете изменить ее по пути: 
todo/main/views.py в представлении feedback.<br> Замените ['umeliere.answer@yandex.ru'] на нужную вам почту.

--- 

<h2>Последнии шаги</h2>

Установить django командой(версия Python >= 3.8, django=4):

```
pip install -r requirements.txt
```

Произвести миграции:
```
python manage.py makemigrations
python manage.py migrate
```

Создать суперпользователя:
```
python manage.py createsuperuser
```

Запустить сервер(по умолчанию http://localhost:8000):
```
python manage.py runserver
```

---
<h3>Работа с API</h3>

Вы можете начать работу с API по <a href="http://127.0.0.1:8000/api/">ссылке</a>. 
Или перейдя к <a href="https://documenter.getpostman.com/view/26760459/2s93XyT3Tv">документации</a> API.

В документации не указано, что работа с пользователями осуществляется по
<a href="http://127.0.0.1:8000/api/users/">ссылке</a> только для пользователей с правами администратора.

---
<h3>При возникновении проблем со входом в админ-панель Django:</h3>

Был добавлен middleware, запрещающий вход пользователям, не являющимися сотрудниками.<br>
Вам нужно войти как <b>superuser</b> и после этого будет открыта админ-панель django.

---