from django.db import models

from core.apps.coins.entities.coins import Coin as CoinEntity
from core.apps.coins.models.base import BaseCollectModel


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

    def to_entity(self) -> CoinEntity:
        return CoinEntity(
            id=self.id,
            title=self.title,
            description=self.description,
            country=self.country,
            issue_at=self.issue_at,
            state=self.state,
            create_at=self.create_at,
            update_at=self.update_at,
        )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Монета'
        verbose_name_plural = 'Монеты'
