from django.db import models

from django.db.models import Model, DateTimeField

# Create your models here.


class AbstractDateTime(Model):
    """AbstractDateTime"""

    datetime_created = DateTimeField(
        verbose_name='Время создания',
        auto_now_add=True
    )
    datetime_updated = DateTimeField(
        verbose_name='Время редактирования',
        auto_now=True
    )
    datetime_deleted = DateTimeField(
        verbose_name='Время удаления',
        null=True,
        blank=True
    )

    class Meta:
        abstract = True

