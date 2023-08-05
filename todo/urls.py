"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls import handler404, handler500
from todo.yasg import urlpatterns as docs

handler404 = "main.views.page_not_found"  # noqa
handler500 = "main.views.server_error"  # noqa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path("users/", include("users.urls")),
    path("users/", include("django.contrib.auth.urls")),
    path("api/v1/", include("api.urls")),
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)),
] + docs

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
