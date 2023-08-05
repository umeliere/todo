from django.urls import re_path, path
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
)
from users.views import (
    registration,
    user_login,
    user_logout,
)


urlpatterns = [
    re_path(r'^registration/', registration, name='registration'),
    re_path(r'^login/', user_login, name='user_login'),
    re_path(r'^logout/', user_logout, name='logout'),

    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
