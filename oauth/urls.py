# imports

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('dashboard/', admin.site.urls),
    path("", include("myapp.urls")),
    path("oauth/", include("allauth.urls")),
]
