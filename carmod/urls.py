from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('categorys', views.category_list, name='category_list'),
    path('parts', views.part_list, name='part_list'),
    path('cars/<int:pk>', views.car_detail, name="car_detail"),
    path('categorys/<int:pk>', views.category_detail, name="category_detail"),
    path('parts/<int:pk>', views.part_detail, name="part_detail"),
    path('cars/new', views.car_create, name='car_create'),
    path('cars/<int:pk>/edit', views.car_edit, name='car_edit'),
    path('cars/<int:pk>/delete', views.car_delete, name='car_delete'),
    path('categorys/new', views.category_create, name='category_create'),
    path('categorys/<int:pk>/edit', views.category_edit, name='category_edit'),
    path('categorys/<int:pk>/delete', views.category_delete, name='category_delete'),
    path('parts/new', views.part_create, name='part_create'),
    path('parts/<int:pk>/edit', views.part_edit, name='part_edit'),
    path('parts/<int:pk>/delete', views.part_delete, name='part_delete'),
]