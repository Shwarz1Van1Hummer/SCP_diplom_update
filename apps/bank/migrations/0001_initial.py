# Generated by Django 4.1.1 on 2022-11-02 10:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='Время редактирования')),
                ('datetime_deleted', models.DateTimeField(blank=True, null=True, verbose_name='Время удаления')),
                ('number', models.CharField(max_length=20, unique=True, verbose_name='Номер счёта')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата открытия')),
                ('balance', models.FloatField(default=0, verbose_name='Баланс')),
            ],
            options={
                'verbose_name': 'Счёт',
                'verbose_name_plural': 'Счета',
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='Время редактирования')),
                ('datetime_deleted', models.DateTimeField(blank=True, null=True, verbose_name='Время удаления')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата транзакции')),
                ('status', models.CharField(choices=[('Обрабатывается', 'Processing'), ('Успешно', 'Ok'), ('Неверно', 'Bad'), ('Ожидание превышено', 'Late'), ('Отклонено', 'Rejected')], default='Обрабатывается', max_length=18, verbose_name='Статус')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Сумма перевода')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='recieve', to='bank.account')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='send', to='bank.account')),
            ],
            options={
                'verbose_name': 'Транзакция',
                'verbose_name_plural': 'Транзакции',
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='Время редактирования')),
                ('datetime_deleted', models.DateTimeField(blank=True, null=True, verbose_name='Время удаления')),
                ('number', models.CharField(max_length=16, unique=True, verbose_name='Номер карты')),
                ('cvv_code', models.CharField(max_length=3, verbose_name='СVV2')),
                ('expirations_date', models.DateField(default=datetime.datetime(2025, 11, 1, 16, 44, 49, 286164), verbose_name='Срок годности')),
                ('balance', models.FloatField(default=0, verbose_name='Баланс')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cards', to='bank.account')),
            ],
            options={
                'verbose_name': 'Карта',
                'verbose_name_plural': 'Карты',
            },
        ),
    ]
