# Generated by Django 5.1.2 on 2024-11-01 10:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=128, verbose_name='Марка автомобиля')),
                ('model', models.CharField(max_length=128, verbose_name='Модель автомобиля')),
                ('year', models.IntegerField(verbose_name='Год выпуска')),
                ('description', models.TextField(max_length=1024, verbose_name='Описание автомобиля')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания записи')),
                ('updated_at', models.DateTimeField(verbose_name='Дата и время последнего обновления записи')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=1024)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания коментария')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Внешний ключ на пользователя')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.car', verbose_name='Внешний ключ на автомобиль')),
            ],
        ),
    ]
