from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=255, verbose_name='Отчество', null=True, blank=True)
    email = models.EmailField(unique=True, db_index=True)
    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return self.get_full_name()

    def get_full_name(self) -> str:
        """ФИО."""
        names = [
            name
            for name in (self.last_name, self.first_name, self.middle_name)
            if name is not None
        ]
        return " ".join(names)
