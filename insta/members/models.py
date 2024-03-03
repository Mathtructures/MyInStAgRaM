from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class genders(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')

    gender = models.CharField(
        max_length=1,
        choices=genders.choices,
        default=genders.MALE,
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'first_name',
                       'last_name', 'email', 'gender']

    def __str__(self):
        return f"{self.first_name} {self.last_name} == as ==> @{self.username}"
