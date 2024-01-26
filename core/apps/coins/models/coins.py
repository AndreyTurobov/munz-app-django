from django.db import models

from core.apps.common.models import BaseCollectModel


class Coin(BaseCollectModel):
    weight = models.CharField(
        verbose_name='Вес монеты',
        max_length=25,
    )
    krauze = models.CharField(
        verbose_name='КМ#',
        max_length=25,
        blank=True,
    )
    state = models.CharField(
        verbose_name='Состояние монеты',
        max_length=25,
    )

    class Meta:
        verbose_name = 'Монета'
        verbose_name_plural = 'Монеты'
