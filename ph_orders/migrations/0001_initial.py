# Generated by Django 2.2.7 on 2019-12-04 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ph_products', '0002_auto_20191204_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_last_name', models.TextField(max_length=100)),
                ('client_name', models.TextField(max_length=100)),
                ('client_middlename', models.TextField(blank=True, max_length=100, null=True)),
                ('client_phone_number', models.TextField(max_length=20)),
                ('client_email', models.TextField(blank=True, max_length=100, null=True)),
                ('delivery_type', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Почта России'), (2, 'CDEK'), (3, 'Самовывоз')], null=True)),
                ('delivery_address', models.TextField(max_length=200)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'В корзине'), (2, 'Создан'), (3, 'Согласован'), (4, 'Оплачен'), (5, 'В пути'), (6, 'Завершен')], default=2)),
                ('comment', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatusChangeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'В корзине'), (2, 'Создан'), (3, 'Согласован'), (4, 'Оплачен'), (5, 'В пути'), (6, 'Завершен')], default=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'изменение статуса заказа',
                'verbose_name_plural': 'изменения статуса заказа',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=1)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('order', models.ForeignKey(on_delete='CASCADE', related_name='basket', to='ph_orders.Order')),
                ('product', models.ForeignKey(on_delete='CASCADE', related_name='sales', to='ph_products.ProductModification')),
            ],
        ),
    ]
