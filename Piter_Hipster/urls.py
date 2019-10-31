#Короче топ тема мы тут определяем, какой гет юзать


from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('catalog/', CatalogAPI.as_view()),
    path('main/', MainAPI.as_view()),
    path('goods/', GoodsAPI.as_view()),
]