from django.db import models

# Create your models here.

TYPE_OF_DELIVERY = (
    (1, 'Почта России'),
    (2, 'CDEK'),
    (3, 'Самовывоз'),
)


# class DeliveryTypes(models.Model):
#     delivery_type = models.CharField(max_length=30, choices=TYPE_OF_DELIVERY)
#     address = models.TextField(max_length=200, blank=True, null=True)
#     price = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)


ORDER_STATUSES = (
    (1, 'В корзине'),
    (2, 'Создан'),
    (3, 'Согласован'),
    (4, 'Оплачен'),
    (5, 'В пути'),
    (6, 'Завершен'),
)
ORDER_DEFAULT_STATUS = 2


class Order(models.Model):
    # client data
    client_last_name = models.TextField(max_length=100)
    client_name = models.TextField(max_length=100)
    client_middlename = models.TextField(max_length=100, blank=True, null=True)
    client_phone_number = models.TextField(max_length=20)
    client_email = models.TextField(max_length=100, blank=True, null=True)
    # delivery data
    delivery_type = models.PositiveSmallIntegerField(choices=TYPE_OF_DELIVERY, blank=True, null=True)
    delivery_address = models.TextField(max_length=200)
    # Index = models.TextField(max_length=6)

    status = models.PositiveSmallIntegerField(choices=ORDER_STATUSES, default=ORDER_DEFAULT_STATUS)
    # id_promocode = models.ForeignKey(Promocodes, blank=True, null=True, on_delete='SET_NULL')
    comment = models.TextField(max_length=500)

    def save(self, *args, **kwargs):
        if self.pk:
            old_state = self.__class__.objects.get(pk=self.pk)
            if old_state.status == self.status:
                return super().save(*args, **kwargs)
        super().save(*args, **kwargs)
        OrderStatusChangeLog.objects.create(order=self, status=self.status)

    @property
    def total_cost(self):
        return self.basket.aggregate(s=models.Sum('cost'))['s']


class OrderStatusChangeLog(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=ORDER_STATUSES, default=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "изменение статуса заказа"
        verbose_name_plural = "изменения статуса заказа"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete='CASCADE', related_name='basket')
    product = models.ForeignKey('ph_products.ProductModification', on_delete='CASCADE', related_name="sales")
    count = models.PositiveIntegerField(default=1)
    cost = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)
