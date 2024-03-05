from uuid import uuid4

from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.guests.entities import Guest


class Guest(TimedBaseModel):
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=12,
        unique=True,
    )
    token = models.CharField(
        verbose_name='Токен',
        max_length=255,
        unique=True,
        default=uuid4,
    )

    def __str__(self) -> str:
        return self.phone

    def to_entity(self) -> Guest:
        return Guest(
            phone=self.phone,
            create_at=self.create_at,
            id=self.pk,
        )

    class Meta:
        verbose_name = 'Гость'
        verbose_name_plural = 'Гости'
