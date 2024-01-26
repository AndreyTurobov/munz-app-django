# Generated by Django 5.0.1 on 2024-01-26 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('country', models.CharField(max_length=255, verbose_name='Страна')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('size', models.CharField(max_length=25, verbose_name='Размер')),
                ('issue_at', models.TimeField(blank=True, verbose_name='Дата выпуска в обращение')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('weight', models.CharField(max_length=25, verbose_name='Вес монеты')),
                ('krauze', models.CharField(blank=True, max_length=25, verbose_name='КМ#')),
                ('state', models.CharField(max_length=25, verbose_name='Состояние монеты')),
            ],
            options={
                'verbose_name': 'Монета',
                'verbose_name_plural': 'Монеты',
            },
        ),
    ]