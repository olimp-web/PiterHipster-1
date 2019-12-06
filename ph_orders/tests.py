from itertools import product

from rest_framework.test import APITestCase
from ph_products.models import Product, ProductModification


class OrderTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.products = [
            Product.objects.create(title="Рубашка", price=200),
            Product.objects.create(title="Шапка", price=150)
        ]
        colors = ('red', 'green', 'blue')
        sizes = ('M', 'L')
        for color, size in product(colors, sizes):
            ProductModification.objects.create(product=cls.products[0], color=color, size=size)
        ProductModification.objects.create(product=cls.products[1], color="black", size="XL")

    def test_create_order(self):
        r = self.client.post('/api/orders/', data={
            'client_name': "Тест",
            'client_last_name': "Тестов",
            'client_middlename': "Тестович",
            'client_phone_number': '+79998034567',
            'delivery_type': 2,
            'delivery_address': "Норильск one love",
            'basket': [
                {"product_id": self.products[0].id, "product_color": "green", "product_size": "M", "count": 1},
                {"product_id": self.products[1].id, "product_color": "black", "product_size": "XL", "count": 1}
            ]
        })
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data['code'], 201)
