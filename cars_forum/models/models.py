from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=128, verbose_name='Марка автомобиля')
    model = models.CharField(max_length=128, verbose_name='Модель автомобиля')
    year = models.IntegerField(verbose_name='Год выпуска')
    description = models.TextField(max_length=1024, verbose_name='Описание автомобиля')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания записи')
    updated_at = models.DateTimeField(verbose_name='Дата и время последнего обновления записи')
    owner = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания коментария')