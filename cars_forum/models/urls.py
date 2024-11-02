from django.urls import path

from .views import (CarCreate, CarEdit, CarDelete, CarList, CarDetail,
                    CommentCreate, CommentEdit, CommentDelete)



urlpatterns = [
    path('car_create/', CarCreate.as_view(), name='car_create'),
    path('car_edit/<int:pk>', CarEdit.as_view(), name='car_edit'),
    path('car_delete/<int:pk>', CarDelete.as_view(), name='car_delete'),
    path('car_detail/<int:pk>', CarDetail.as_view(), name='car_detail'),
    path('', CarList.as_view(), name='car_list'),

    path('comment_create/', CommentCreate.as_view(), name='comment_create'),
    path('comment_edit/<int:pk>', CommentEdit.as_view(), name='comment_edit'),
    path('comment_delete/<int:pk>', CommentDelete.as_view(), name='comment_delete')
]