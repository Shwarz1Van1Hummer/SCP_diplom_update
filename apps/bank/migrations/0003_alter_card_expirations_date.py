# Generated by Django 4.0.6 on 2022-12-13 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='expirations_date',
            field=models.DateField(default=datetime.datetime(2025, 12, 12, 20, 11, 35, 63100), verbose_name='Срок годности'),
        ),
    ]
