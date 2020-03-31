from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.TextField(max_length=100)
    cover_image = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Product(models.Model):

    title = models.TextField(max_length=100, verbose_name="название товара")
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name="описание")
    category = models.ForeignKey('ph_products.Category', verbose_name='категория',
                                 on_delete='SET_NULL', blank=True, null=True)
    price = models.FloatField(verbose_name="цена")
    left_in_stock = models.IntegerField(verbose_name="осталось на складе", default=1)
    prime_cost = models.FloatField(blank=True, verbose_name="себестоимость", default=0)

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"


class ProductPhoto(models.Model):
    product = models.ForeignKey('ph_products.Product', on_delete='CASCADE', related_name="photos")
    image = models.ImageField()
    is_main = models.BooleanField(default=False)
    alt = models.TextField(max_length=100, default='Product picture')

    class Meta:
        verbose_name = "фото товара"
        verbose_name_plural = "фото товаров"


TYPE_OF_SIZE = (
    ('XXS', 'XXSmall'),
    ('XS', 'XSmall'),
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'XLarge'),
    ('XXL', 'XXLarge'),
    ('NO', 'Without size'),
)


class ProductModification(models.Model):
    product = models.ForeignKey(Product, on_delete='CASCADE', related_name="modifications")
    color = models.TextField(max_length=100)
    size = models.TextField(max_length=30, choices=TYPE_OF_SIZE)
    left_in_stock = models.IntegerField(verbose_name="осталось на складе", default=1)

    class Meta:
        verbose_name = "модификация"
        verbose_name_plural = "модификации товара"
