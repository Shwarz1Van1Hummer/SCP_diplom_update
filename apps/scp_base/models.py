
from django.db import models
from django.db.models.query import QuerySet
from typing import Optional, Any
from datetime import datetime
from abstracts.models import AbstractDateTime
from django.db.models.signals import pre_save, post_save, post_delete


class ScpModelQuerySet(QuerySet):

    def get_deleted(self) -> QuerySet['SCPSafe']:
        return self.filter(datetime_deleted_isnull=False)

    def get_not_deleted(self) -> QuerySet['SCPSafe']:
        return self.filter(
            datetime_deleted__isnull=True
        )

    def get_not_equal_updated(self) -> QuerySet:
        return self.filter(
            datetime_updated=['datetime_created']
        )

    def get_obj(self, p_key: str) -> Optional['SCPSafe']:
        try:
            return self.get(
                id=p_key
            )
        except SCPSafe.DoesNotExist:
            return None


class SCPSafe(AbstractDateTime, models.Model):
    title_object = models.CharField(verbose_name='Название объекта', max_length=100)
    description = models.CharField(verbose_name='Описание', max_length=6000)
    image = models.ImageField(verbose_name='Изображение', upload_to='scp_safe')
    content = models.CharField(verbose_name="Условия содержания", max_length=5000)

    objects = ScpModelQuerySet().as_manager()

    class Meta:
        ordering = (
            'title_object',
        )
        verbose_name = 'Безопасный объект'
        verbose_name_plural = 'Безопасные объекты'

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.full_clean()
        super().save(*args, **kwargs)

    def delete(self) -> None:
        self.datetime_deleted = datetime.now()
        self.save()

    def __str__(self):
        return f'{self.title_object}'
#Целый ____________________


class SCPEuclid(AbstractDateTime, models.Model):
    title_object = models.CharField(verbose_name='Название объекта фонда', max_length=255)
    description = models.CharField(verbose_name='Описание', max_length=6000)
    image = models.ImageField(verbose_name="Изображение", upload_to='scp_euclid/')
    content = models.CharField(verbose_name="Условия содержания", max_length=5000)

    objects = ScpModelQuerySet().as_manager()

    class Meta:
        ordering = (
            'title_object',
        )
        verbose_name = 'Объект класса Евклид'
        verbose_name_plural = 'Объекты класса Еклид'

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.full_clean()
        super().save(*args, **kwargs)

    def delete(self) -> None:
        self.datetime_deleted = datetime.now()
        self.save()

    def __str__(self):
        return f'{self.title_object}'


class SCPKeter(AbstractDateTime,models.Model):
    title_object = models.CharField(verbose_name='Название объекта фонда', max_length=255)
    description = models.CharField(verbose_name='Описание', max_length=6000)
    image = models.ImageField(verbose_name="Изображение", upload_to='scp_keter')
    content = models.CharField(verbose_name="Условия содержания", max_length=5000)

    objects = ScpModelQuerySet().as_manager()

    class Meta:
        ordering = (
            'title_object',
        )
        verbose_name = 'Объект класса Кетер'
        verbose_name_plural = 'Объекты класса Кетер'

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.full_clean()
        super().save(*args, **kwargs)

    def delete(self) -> None:
        self.datetime_deleted = datetime.now()
        self.save()

    def __str__(self):
        return f'{self.title_object}'


class SCPThaumiel(AbstractDateTime,models.Model):
    title_object = models.CharField(verbose_name='Название объекта фонда', max_length=255)
    description = models.CharField(verbose_name='Описание', max_length=6000)
    image = models.ImageField(verbose_name="Изображение", upload_to='scp_thaumiel/')
    content = models.CharField(verbose_name="Условия содержания", max_length=5000)

    objects = ScpModelQuerySet().as_manager()

    class Meta:
        ordering = (
            'title_object',
        )
        verbose_name = 'Объект класса таумиель'
        verbose_name_plural = 'Объекты класса таумиель'

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.full_clean()
        super().save(*args, **kwargs)

    def delete(self) -> None:
        self.datetime_deleted = datetime.now()
        self.save()

    def __str__(self):
        return f'{self.title_object}'


class SCPAllClasses(AbstractDateTime,models.Model):
    scp_safe = models.ForeignKey(SCPSafe, verbose_name='Объект класса Безопасный', on_delete=models.PROTECT)
    scp_euclid = models.ForeignKey(SCPEuclid, verbose_name='Объект класса Евклид', on_delete=models.PROTECT)
    scp_keter = models.ForeignKey(SCPKeter, verbose_name='Объект класса Кетер', on_delete=models.PROTECT)
    scp_thaumiel = models.ForeignKey(SCPThaumiel, verbose_name='Объект класса Таумиель', on_delete=models.PROTECT)

    objects = ScpModelQuerySet().as_manager()

    class Meta:
        ordering = (
            'id',
        )
        verbose_name = 'Все объекты фонда'

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.full_clean()
        super().save(*args, **kwargs)

    def delete(self) -> None:
        self.datetime_deleted = datetime.now()
        self.save()

    def __str__(self):
        return f'{self.id}'


class NewsSCP(models.Model):
    message_scp = models.SlugField(blank=True, null=True)

    def __str__(self):
        return f'{self.message_scp}'


def safe_post_save(sender, instance, created, *args, **kwargs):
    if created:
        news_scp = NewsSCP.objects.create(
            message_scp=f"Добавление объекта SCP {instance.title_object}. "              
                    "Подробную информацию вы можете изучить в списке классов объектов ФОНДА"
        )
        news_scp.save()


post_save.connect(safe_post_save, sender=SCPSafe)
post_save.connect(safe_post_save, sender=SCPEuclid)
post_save.connect(safe_post_save, sender=SCPKeter)
post_save.connect(safe_post_save, sender=SCPThaumiel)


def safe_post_delete(sender, instance, deleted, *args, **kwargs):
    if deleted:
        news_scp = NewsSCP.objects.create(
            message_scp=f"Удаления объекта SCP {instance.title_object}. "
                          f"Данные объекта были удалены связи с решением совета О5."

        )
        news_scp.save()


post_delete.connect(safe_post_save, sender=SCPSafe)
