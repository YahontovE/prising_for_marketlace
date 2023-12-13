from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    login_as = models.BooleanField(default=False, verbose_name='авторизоваться как')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
