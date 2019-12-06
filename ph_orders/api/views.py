from rest_framework.generics import CreateAPIView

from ph_orders.models import Order
from .serializers import OrderSerializer

from helpers.views import StatusOnly200Mixin


class CreateOrderAPIView(StatusOnly200Mixin, CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
