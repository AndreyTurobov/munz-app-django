from django.db import models

from core.apps.common.models import TimedBaseModel


class Review(TimedBaseModel):
    guest = models.ForeignKey(
        to='guests.Guest',
        on_delete=models.CASCADE,
        related_name='coin_reviews',
        verbose_name='Автор отзыва',
    )
    text = models.TextField(
        verbose_name='Текст отзыва',
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

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        unique_together = (('guest', 'coin'),)
