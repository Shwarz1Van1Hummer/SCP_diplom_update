from django.db import models
from users.models import CustomUser
from datetime import datetime, timedelta
from abstracts.models import AbstractDateTime


class Account(AbstractDateTime, models.Model):
    owner = models.ForeignKey(
        CustomUser, related_name='accounts', on_delete=models.PROTECT
    )
    number = models.CharField(
        verbose_name='Номер счёта', max_length=20, unique=True, null=False
    )
    date = models.DateField(
        verbose_name='Дата открытия', auto_now_add=True,
    )
    balance = models.FloatField(
        verbose_name='Баланс', default=0,
    )

    def __str__(self):
        return f'{self.owner} : {self.number}'

    class Meta:
        verbose_name = 'Счёт'
        verbose_name_plural = 'Счета'


class Transactions(AbstractDateTime, models.Model):
    class StatusTransaction(models.TextChoices):
        PROCESSING = 'Обрабатывается'
        OK = 'Успешно'
        BAD = "Неверно"
        LATE = "Ожидание превышено"
        REJECTED = "Отклонено"

    sender = models.ForeignKey(Account, related_name='send', on_delete=models.PROTECT)
    receiver = models.ForeignKey(Account, related_name='recieve', on_delete=models.PROTECT)
    date = models.DateTimeField(verbose_name='Дата транзакции', auto_now_add=True)
    status = models.CharField(verbose_name="Статус", max_length=18, choices=StatusTransaction.choices, default=StatusTransaction.PROCESSING)
    amount = models.DecimalField(verbose_name='Сумма перевода', max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.sender}--> {self.receiver}: {self.amount}'

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = "Транзакции"


class Card(AbstractDateTime, models.Model):
    account = models.ForeignKey(Account, related_name='cards', on_delete=models.PROTECT)
    number = models.CharField(
        verbose_name='Номер карты', max_length=16, unique=True,
    )
    cvv_code = models.CharField(verbose_name='СVV2', max_length=3)
    expirations_date = models.DateField(
        verbose_name='Срок годности', default=(datetime.now() + timedelta(days=365 * 3))
        )

    balance = models.FloatField(verbose_name='Баланс', default=0)

    def __str__(self) -> str:
        return f'{self.number}'

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = "Карты"

