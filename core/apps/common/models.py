from django.db import models


class BaseCollectModel(models.Model):
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
    issue_at = models.TimeField(
        verbose_name='Дата выпуска в обращение',
        blank=True,
    )
    create_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )
    update_at = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True,
    )
    
    class Meta:
        abstract = True
    