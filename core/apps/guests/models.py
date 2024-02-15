from uuid import uuid4

from django.db import models

from core.apps.guests.entities import GuestEntity


class Guest(models.Model):
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
    create_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )
    update_at = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True,
    )

    def __str__(self) -> str:
        return self.phone

    def to_entity(self) -> GuestEntity:
        return GuestEntity(
            phone=self.phone,
            create_at=self.create_at,
        )

    class Meta:
        verbose_name = 'Гость'
        verbose_name_plural = 'Гости'
