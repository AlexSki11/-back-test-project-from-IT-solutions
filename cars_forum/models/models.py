from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

import datetime

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=128, verbose_name='Марка автомобиля')
    model = models.CharField(max_length=128, verbose_name='Модель автомобиля')
    year = models.IntegerField(verbose_name='Год выпуска')
    description = models.TextField(max_length=1024, verbose_name='Описание автомобиля')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания записи')
    updated_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата и время последнего обновления записи', blank=True)
    owner = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='owner')

    def get_absolute_url(self):
        return reverse("car_detail", kwargs={"pk": self.pk})
    
    def update_date(self):
        self.updated_at=timezone.now()
        
    

class Comment(models.Model):
    content = models.TextField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания коментария')
    car = models.ForeignKey(Car, verbose_name='Внешний ключ на автомобиль', on_delete=models.CASCADE, related_name='car')
    author = models.ForeignKey(User, verbose_name='Внешний ключ на пользователя', on_delete=models.CASCADE, related_name='author')
