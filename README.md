<h1>Инструкция по установки ToDo</h1>

<h2>Установить к себе репозиторий:</h2>

```
git clone https://github.com/umeliere/todo.git
```

---

<h4>Создать файл .env в папке todo/todo(где находится файл settings.py)<br>
В него занести следующие данные:<br></h4>

```
DEBUG=True
SECRET_KEY=django-insecure-y6_c-qq19+pl_a2_=v*41%^r^1(6525ar+vge8ku&!)-c%)lz!

EMAIL_HOST=XXXXX
EMAIL_PORT=XXXXX
EMAIL_HOST_USER=XXXXX
DEFAULT_FROM_EMAIL=XXXXX
EMAIL_HOST_PASSWORD=XXXXX
EMAIL_USE_SSL=XXXXX
```
---
<h3>Вам нужно подключить YANDEX smtp, ДОКУМЕНТАЦИЯ:</h3>
http://help.yandex.ru/mail/mail-clients.xml
<p>И заполнить поля:</p>

```
EMAIL_HOST=XXXXX
EMAIL_PORT=XXXXX
EMAIL_HOST_USER=XXXXX
DEFAULT_FROM_EMAIL=XXXXX
EMAIL_HOST_PASSWORD=XXXXX
EMAIL_USE_SSL=XXXXX
```

Если вы не хотите пользоваться yandex smpt, вы всегда можете сменить на любой удобный почтовый сервис</p>

https://docs.djangoproject.com/en/4.2/topics/email/  -- Документация

---
<h2>Последнии шаги</h2>

Установить django командой(версия Python >= 3.8, django=4.0):

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

<h3>При возникновении проблем со входом в админ-панель Django:</h3>

Был добавлен middleware, запрещающий вход пользователям, не являющимися сотрудниками.<br>
Вам нужно войти как <b>superuser</b> и после этого будет открыта админ-панель django.

---
<h3>Документация к API доступна по ссылке: http://127.0.0.1:8000/swagger/ </h3>

---