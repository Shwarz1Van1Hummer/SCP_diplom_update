from django.dispatch import receiver
from django.db.models.base import ModelBase
from typing import Any
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from .models import News
from scp_base.models import SCPSafe


@receiver(post_save, sender=SCPSafe)
def create_news(sender, instance, created, **kwargs):
    if created:
        News.objects.create(
            description=f'В базу данных фонда был добавлен новый объект'
                        f'{instance.title_object}')




    # return f'{title}\n' \
    #        f'{description}'
