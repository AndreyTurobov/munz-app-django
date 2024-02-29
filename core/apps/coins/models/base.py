from django.db import models

from core.apps.common.models import TimedBaseModel


class BaseCollectModel(TimedBaseModel):
    title = models.CharField(
        max_length=255,
        verbose_name='Название',
    )
    country = models.CharField(
        max_length=255,
        verbose_name='Страна',
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
    )
    size = models.CharField(
        verbose_name='Размер',
        max_length=25,
    )
    issue_at = models.CharField(
        verbose_name='Дата выпуска в обращение',
    )

    class Meta:
        abstract = True
