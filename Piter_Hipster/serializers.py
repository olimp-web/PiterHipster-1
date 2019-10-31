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



class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = ("Direction", "alt")

class ModificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modifications
        fields=("color", "size")

class GoodsAdminSerializers(serializers.ModelSerializer):
    id_category = CategorySerializer
    photos = PhotoSerializer(many=True, read_only=True)
    class Meta:
        model = Goods
        fields = ("id", "Title", "Description", "id_category", "Price", "Left_in_stock", "Prime_cost", "photos")

class GoodsBuyerSerializers(serializers.ModelSerializer):
    id_category = CategorySerializer
    photos = PhotoSerializer(many=True, read_only=True)
    modifications = ModificationsSerializer(many=True, read_only=True)
    class Meta:
        model = Goods
        fields = ("id", "Title", "Description", "Price", "photos", "modifications")

class GoodsCatalogSerializers(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()
    class Meta:
        model = Goods
        fields = ("id", "Title", "Price", "photos")
    def get_photos(self, obj):
        serializer = PhotoSerializer(obj.photos.filter(isMain=True), many=True, read_only=True)
        return  serializer.data

class GoodsInOrderPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsInOrders
        fields = ("Count", "Price")

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ("Type_delivery", "Address", "Price")

class OrdersPostSerializer(serializers.ModelSerializer):
    goodsInOrders = GoodsInOrderPostSerializer(read_only=True, many=True)
    id_delivery = DeliverySerializer(read_only=True)
    Middlename = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    Comment = serializers.CharField(required=False)

    class Meta:
        model = Orders
        fields = ("id", "Name", "Lastname", "Middlename", "Phone", "email", "id_delivery", "Address", "status", "Index",
                  "Date_of_order", "goodsInOrders", "Comment")

