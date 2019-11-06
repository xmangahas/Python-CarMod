from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('categorys', views.category_list, name='category_list'),
    path('parts', views.part_list, name='part_list'),
]