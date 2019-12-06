from rest_framework import serializers
from ph_orders.models import Order, OrderItem
from ph_products.models import ProductModification


class OrderItemSerializer(serializers.Serializer):
    count = serializers.IntegerField(min_value=1)
    product_color = serializers.CharField()
    product_size = serializers.CharField()
    product_id = serializers.IntegerField()

    class Meta:
        fields = ('count', 'product_id', 'product_color', 'product_size')


class OrderSerializer(serializers.ModelSerializer):
    basket = OrderItemSerializer(many=True, write_only=True)
    client_email = serializers.EmailField(required=False)

    class Meta:
        model = Order
        fields = ('client_last_name', 'client_name', 'client_middlename', 'client_phone_number', 'client_email',
                  'delivery_type', 'delivery_address', 'basket')

    def create(self, validated_data):
        items = validated_data.pop('basket')
        order = super().create(validated_data)
        for item in items:
            product_mod = ProductModification.objects.get(
                product_id=item['product_id'],
                color=item['product_color'],
                size=item['product_size']
            )
            OrderItem.objects.create(product=product_mod, count=item['count'], order=order)
        return order
