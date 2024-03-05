from django.db import models

from core.apps.coins.entities.coins import Coin as CoinEntity
from core.apps.coins.entities.reviews import Review as ReviewEntity
from core.apps.common.models import TimedBaseModel
from core.apps.guests.entities import Guest as GuestEntity


class Review(TimedBaseModel):
    guest = models.ForeignKey(
        to='guests.Guest',
        on_delete=models.CASCADE,
        related_name='coin_reviews',
        verbose_name='Автор обзора',
    )
    text = models.TextField(
        verbose_name='Текст обзора',
        blank=True,
        default='',
        max_length=500,
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name='Оценка',
        default=1,
    )
    coin = models.ForeignKey(
        to='coins.Coin',
        on_delete=models.CASCADE,
        related_name='coin_reviews',
        verbose_name='Монета',
    )

    # TODO: Send only review
    @classmethod
    def from_entity(
        cls,
        review: ReviewEntity,
        guest: GuestEntity,
        coin: CoinEntity,
    ) -> 'Review':
        return cls(
            pk=review.id,
            coin_id=coin.id,
            guest_id=guest.id,
            text=review.text,
            rating=review.rating,
        )

    def to_entity(self) -> ReviewEntity:
        return ReviewEntity(
            id=self.pk,
            text=self.text,
            rating=self.rating,
            create_at=self.create_at,
            update_at=self.update_at,
        )

    class Meta:
        verbose_name = 'Обзор'
        verbose_name_plural = 'Обзоры'
        unique_together = (('guest', 'coin'),)
