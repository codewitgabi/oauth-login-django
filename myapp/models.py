# imorts

import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False)
	username = models.CharField(max_length=30)
	email = models.EmailField(unique=True)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ["username"]

	def __str__(self):
	    return self.email

