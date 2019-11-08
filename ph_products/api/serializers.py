from rest_framework import serializers
from django.contrib.auth.models import User
from ph_products.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title")


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ("image", "alt")


class ModificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModification
        fields = ("color", "size")


class ShortProductSerializer(serializers.ModelSerializer):
    """Для списка товаров"""
    photos = PhotoSerializer(many=True, read_only=True)
    category = CategorySerializer()
    in_stock = serializers.BooleanField(source='left_in_stock')

    class Meta:
        model = Product
        fields = ("id", "title", "price", "photos")


class FullProductSerializer(ShortProductSerializer):
    """Для страницы товара"""
    modifications = ModificationSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ("id", "title", "description", "price", "photos", "modifications")


# class GoodsAdminSerializers(serializers.ModelSerializer):
#     id_category = CategorySerializer
#     photos = PhotoSerializer(many=True, read_only=True)
#     class Meta:
#         model = Goods
#         fields = ("id", "Title", "Description", "id_category", "Price", "Left_in_stock", "Prime_cost", "photos")
#
#
# class GoodsBuyerSerializers(serializers.ModelSerializer):
#     id_category = CategorySerializer
#     photos = PhotoSerializer(many=True, read_only=True)
#     modifications = ModificationsSerializer(many=True, read_only=True)
#     class Meta:
#         model = Goods
#         fields = ("id", "Title", "Description", "Price", "photos", "modifications")
#
#
# class GoodsCatalogSerializers(serializers.ModelSerializer):
#     photos = serializers.SerializerMethodField()
#     class Meta:
#         model = Goods
#         fields = ("id", "Title", "Price", "photos")
#     def get_photos(self, obj):
#         serializer = PhotoSerializer(obj.photos.filter(isMain=True), many=True, read_only=True)
#         return  serializer.data
