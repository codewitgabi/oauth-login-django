# imports

from django.urls import path
from . import views


app_name = "account"
urlpatterns = [
    path("", views.sign_in_with_oauth, name="oauth_signin"),
]
