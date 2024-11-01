from django.urls import path

from .views import (CarCreate, CarEdit, CarDelete, CarList, CarDetail)



urlpatterns = [
    path('car_create/', CarCreate.as_view(), name='car_create'),
    path('car_edit/<int:pk>', CarEdit.as_view(), name='car_edit'),
    path('car_delete/<int:pk>', CarDelete.as_view(), name='car_delete'),
    path('car_detail/<int:pk>', CarDetail.as_view(), name='car_detail'),
    path('', CarList.as_view(), name='car_list'),
]