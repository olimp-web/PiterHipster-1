# python manage.py makemigrations Piter_Hipster
# python manage.py migrate Piter_Hipster
# python manage.py migrate --fake myappname zero
# ./manage.py migrate --fake-initial чтобы прога поняла, что мы уже ту миграцию выполняли


from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    Title = models.TextField(max_length=100)


class Goods(models.Model):

    Title = models.TextField(max_length=100)
    Description = models.TextField(max_length=500, blank=True, null=True)
    id_category = models.ForeignKey(Categories, verbose_name='Код', on_delete='SET_NULL', blank=True, null=True)
    Price = models.FloatField()
    Left_in_stock = models.IntegerField()
    Prime_cost = models.FloatField()

class Photos(models.Model):
    id_goods = models.ForeignKey(Goods, on_delete='CASCADE', related_name="photos")
    Direction = models.TextField(max_length=500)
    isMain = models.BooleanField(default=False)
    alt = models.TextField(max_length=100, default='picture')


class Marks(models.Model):
    Title = models.TextField(max_length=100)


class MarkGoods(models.Model):
    id_mark = models.ForeignKey(Marks, on_delete='CASCADE')
    id_goods = models.ForeignKey(Goods, on_delete='CASCADE')




TYPE_OF_DELIVERY = (
    ('Почта России', 'Почта России'),
    ('CDEK', 'CDEK'),
    ('Самовывоз', 'Самовывоз'),

)


class Delivery(models.Model):
    Type_delivery = models.CharField(max_length=30, choices=TYPE_OF_DELIVERY)
    Address = models.TextField(max_length=200, blank=True, null=True)
    Price = models.FloatField(blank=True, null=True)


TYPE_OF_SALE = (
    ('Фиксированная', 'Фиксированная'),
    ('Процент', 'Процент'),
)


class Sale(models.Model):
    Title = models.TextField(max_length=100)
    Type_sale = models.CharField(max_length=30, choices=TYPE_OF_SALE)
    Size = models.FloatField()
    Min_price = models.FloatField(blank=True, null=True)
    Lim_cat = models.ForeignKey(Categories, blank=True, null=True, on_delete='SET_NULL')
    Lim_start_date = models.DateField(blank=True, null=True)
    Lim_end_date = models.DateField(blank=True, null=True)
    Lim_goods = models.ForeignKey(Goods, blank=True, null=True, on_delete='SET_NULL')
    Lim_mark = models.ForeignKey(Marks, blank=True, null=True, on_delete='SET_NULL')


class Promocodes(models.Model):
    Title = models.TextField(max_length=100)
    id_sale = models.ForeignKey(Sale, blank=True, null=True, on_delete='CASCADE')


class Distribution(models.Model):
    email = models.EmailField()


TYPE_OF_STATUS = (
    ('В корзине', 'В корзине'),
    ('Создан', 'Создан'),
    ('Согласован', 'Согласован'),
    ('Оплачен', 'Оплачен'),
    ('В пути', 'В пути'),
    ('Завершен', 'Завершен'),
)


class Orders(models.Model):
    Lastname = models.TextField(max_length=100)
    Name = models.TextField(max_length=100)
    Middlename = models.TextField(max_length=100, blank=True, null=True)
    Phone = models.TextField(max_length=20)
    email = models.TextField(max_length=100, blank=True, null=True)
    id_delivery = models.ForeignKey(Delivery, blank=True, null=True, on_delete='SET_NULL')
    status = models.CharField(max_length=30, choices=TYPE_OF_STATUS, default='В корзине')
    id_promocode = models.ForeignKey(Promocodes, blank=True, null=True, on_delete='SET_NULL')
    Address = models.TextField(max_length=200)
    Index = models.TextField(max_length=6)
    Date_of_payment = models.DateTimeField(blank=True, null=True)
    Date_of_create = models.DateTimeField(auto_now_add=True)
    Date_of_order = models.DateTimeField(blank=True, null=True)
    Comment = models.TextField(max_length=500)


class GoodsInOrders(models.Model):
    id_goods = models.ForeignKey(Goods, on_delete='CASCADE')
    Count = models.IntegerField(default=1)
    Price = models.FloatField()
    id_order = models.ForeignKey(Orders, on_delete='CASCADE', related_name='goodsInOrders')

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

class Modifications(models.Model):
    id_goods = models.ForeignKey(Goods, on_delete='CASCADE', related_name="modifications")
    color = models.TextField(max_length=100)
    size = models.TextField(max_length=30, choices=TYPE_OF_SIZE)

