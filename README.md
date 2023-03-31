<h1>Инструкция по установки todo...</h1>

---

Создать файл .env в папке todo/todo(где находится файл settings.py)<br>
В него занести следующие данные:<br>
```
DEBUG=True
```

Сгенерировать секретный ключ - https://djecrety.ir/
```
SECRET_KEY=django-insecure-сгенерированный ключ<br>
```

Пример: 
```
SECRET_KEY=django-insecure-f!o7l(696(z@!3i)k37w0w&#63k0tzaw40)2a84wr424yoq86j
```

<h2>Настройка smtp</h2>
https://wiki.donapex.net/mail/mail-send/ - сайт для помощи настройки smtp  <br>

```
EMAIL_HOST=сервер почтового сервиса
EMAIL_PORT=порт почтового сервиса
EMAIL_HOST_USER=ваша почта
DEFAULT_FROM_EMAIL=ваша почта
EMAIL_HOST_PASSWORD=пароль от вашей почты
EMAIL_USE_SSL=True  # может использоваться тип соединения TLS
```

После данных операций нужно установить библиотеку environ:<br>
```
pip install django-environ
```

Также в todo/main/views.py указать почту с поля EMAIL_HOST_USER вместо поля 'email_host_user'(обязательно в кавычках)
и почту, на которую будут приходить письма вместо поля ['personal mail'] (обязательно в квадратных скобках и кавычках)

--- 

<h2>Следующий этап</h2>

Установить django командой(версия Python >= 3.8, django=4):

```
pip install -r requirements.txt
```

Произвести миграции:
```
python3 manage.py makemigrations
```
И
```
python3 manage.py migrate
```

Запустить сервер(по умолчанию http://localhost:8000):
```
python3 manage.py runserver
```


