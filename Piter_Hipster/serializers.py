#Обработка данных из бд

from rest_framework import serializers
from django.contrib.auth.models import User
from Piter_Hipster.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ("id", "Title")

class GoodsAdminSerializers(serializers.ModelSerializer):
    id_category = CategorySerializer
    class Meta:
        model = Goods
        fields = ("id", "Title", "Description", "id_category", "Price", "Left_in_stock", "Prime_cost")

class PhotoSerializer(serializers.ModelSerializer):
    fields = ("id", "Directory")

class GoodsBuyerSerializers(serializers.ModelSerializer):
    id_category = CategorySerializer
    class Meta:
        model = Goods
        fields = ("id", "Title", "Description", "id_category", "Price")
