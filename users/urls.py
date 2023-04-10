from django.urls import re_path
from .views import *


urlpatterns = [
    re_path(r'^registration/', registration, name='registration'),
    re_path(r'^login/', user_login, name='user_login'),
    re_path(r'^logout/', user_logout, name='logout'),
]
