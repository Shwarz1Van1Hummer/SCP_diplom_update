from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.db.models.query import QuerySet
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
import datetime
from datetime import timedelta
import jwt
from django.conf import settings


class CustomUserManager(BaseUserManager):

    def create_user(self, email: str, password: str) -> 'CustomUser':
        if not email:
            raise ValidationError('Email required')
        user: 'CustomUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str) -> 'CustomUser':
        user: 'CustomUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_info(self):
        print('Custom User Manager')

    def get_search_user_personal(self):
        users: QuerySet(['CustomUser']) = self.filter(
            Q(is_staff=True) &
            Q(data_joined__gte=datetime.date(2022, 7, 1))
        )
        return users


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Почта/Логин', unique=True)
    number = models.CharField('Номер телефона', max_length=11)
    is_staff = models.BooleanField('Статус менеджера', default=False)
    is_active = models.BooleanField('Активность', default=True)
    date_joined = models.DateField('Время создания', default=timezone.now)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'

    class Meta:
        ordering = (
            'date_joined',
        )
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'