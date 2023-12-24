from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=100, verbose_name='почта', unique=True)
    is_active = models.BooleanField(verbose_name='активность', default=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'
