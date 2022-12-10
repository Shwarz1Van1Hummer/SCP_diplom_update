from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.base import ModelBase
from typing import Any
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from .models import CustomUser

@receiver(
    post_save,
    sender=CustomUser
)
def post_save_user(
        sender: ModelBase,
        instance: CustomUser,
        created: bool,
        **kwargs: Any
        ):
    print('POST SaVE called')
    send_mail(
        'Добро пожаловать в секретный фонд SCP, на данном сайте вы можете ввести свой вклад в развитие фонда SCP'
        'Для обеспечения безопасности и дальнейшего изучения SCP-объектов'
        'shwarzvanhummer@gmail.com',
        ['shwarzvanhummer@gmail.com'],
        fail_silently=False

    )
