from django.dispatch import receiver
from django.db.models.base import ModelBase
from typing import Any
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from .models import SCPSafe

# @receiver(
#     post_save,
#     sender=SCPSafe
# )

